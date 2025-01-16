import cv2
import numpy as np
from ultralytics import YOLO
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Параметры
video_path = 'test_720p.mp4'
output_path = './output_recording.avi'
excel_path = './crossroad_monitoring_results.xlsx'
fps = 30  # Частота кадров
recording_duration = 30  # Длительность записи в секундах
max_frames = fps * recording_duration  # Максимум кадров для записи (30 секунд * 30 кадров)

# Определяем линии
zone_width = 30  # ширина зоны
zones = [
    [(977, 553), (966, 573), (1025, 602), (1036, 581)],
    [(997, 506), (983, 524), (1014, 537), (1026, 516)],
    [(654, 391), (638, 412), (683, 436), (701, 415)],
    [(361, 234), (343, 234), (344, 207), (360, 205)],
    [(856, 555), (874, 531), (924, 552), (903, 582)],
    [(228, 206), (211, 218), (237, 232), (246, 214)],
    [(287, 207), (271, 223), (306, 242), (318, 224)],
    [(159, 168), (181, 179), (207, 157), (188, 141)],
    [(183, 114), (205, 127), (225, 112), (208, 100)]
]

# Словари для подсчета машин по классам для каждой зоны
vehicle_classes = ['bus', 'car', 'motobike', 'road_train', 'truck']
vehicle_classes_rus = ['Автобус', 'Легковые', 'Мотоциклы и велосипеды', 'Автопоезда', 'Грузовые']
zone_counters = [{"zone_number": i + 1, **{cls: 0 for cls in vehicle_classes}} for i in range(len(zones))]

# Загрузка модели YOLOv8 с включенным трекингом
model = YOLO('yolov8s_1280_720.pt', verbose=False)

# Словарь для хранения ID объектов, которые пересекли каждую зону
crossed_ids = [defaultdict(set) for _ in zones]

# Проверка, находится ли центр объекта внутри зоны
def is_inside_zone(center, zone):
    return cv2.pointPolygonTest(np.array(zone, dtype=np.int32), center, False) >= 0

# Открываем видео
cap = cv2.VideoCapture(video_path)
width, height = 1280, 720

# Настройка записи видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

prev_positions = {}
frame_count = 0

while cap.isOpened() and frame_count < max_frames:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (width, height))
    results = model.track(frame, persist=True, verbose=False)[0]

    # Получаем боксы и ID трекинга
    boxes = results.boxes.xywh.cpu()
    track_ids = results.boxes.id.int().cpu().tolist()
    class_ids = results.boxes.cls.int().cpu().tolist()

    for box, track_id, class_id in zip(boxes, track_ids, class_ids):
        class_name = model.names[class_id]
        x, y, w, h = box

        if class_name in vehicle_classes:
            curr_center = (int(x), int(y))

            # Отрисовка прямоугольника и ID
            top_left = (int(x - w / 2), int(y - h / 2))
            bottom_right = (int(x + w / 2), int(y + h / 2))
            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)  # Прямоугольник вокруг объекта
            cv2.putText(frame, f"ID: {track_id}", (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)  # Отображаем ID над объектом

            if track_id in prev_positions:
                prev_center = prev_positions[track_id]

                # Проверяем пересечение с каждой зоной
                for i, zone in enumerate(zones):
                    if is_inside_zone(curr_center, zone):
                        if track_id not in crossed_ids[i][class_name]:
                            zone_counters[i][class_name] += 1
                            crossed_ids[i][class_name].add(track_id)
                            print(
                                f"Зона {i + 1}, Класс {class_name}, ID {track_id}, Счет: {zone_counters[i][class_name]}"
                            )

            prev_positions[track_id] = curr_center

    # Отображаем зоны и текущее количество пересечений
    for i, zone in enumerate(zones):
        cv2.polylines(frame, [np.array(zone, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)

        # Вывод количества пересечений для текущей зоны
        text = f"Zone {i + 1}: "
        counts = ', '.join([f"{cls}={zone_counters[i][cls]}" for cls in vehicle_classes])
        cv2.putText(frame, f"{text} {counts}", (zone[0][0], zone[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                    (255, 255, 255), 1)

    # Пишем кадр в файл
    out.write(frame)
    frame_count += 1

    # Отображаем текущий кадр с помощью matplotlib
    clear_output(wait=True)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Отключаем оси
    plt.show()

# Освобождаем ресурсы
cap.release()
out.release()

# Сохранение данных в Excel
# Подготовка данных для записи в Excel
data = []
for i, zone_count in enumerate(zone_counters):
    row = {
        "Зона": f"Зона {zone_count['zone_number']}",
        vehicle_classes_rus[0]: zone_count['bus'],
        vehicle_classes_rus[1]: zone_count['car'],
        vehicle_classes_rus[2]: zone_count['motobike'],
        vehicle_classes_rus[3]: zone_count['road_train'],
        vehicle_classes_rus[4]: zone_count['truck']
    }
    data.append(row)

# Сохранение данных в Excel
df = pd.DataFrame(data)
df.to_excel(excel_path, index=False)
print(f"Данные сохранены в {excel_path}")
