import os
import shutil
import random
import json


def load_classes(classes_file):
    """Загружает классы из файла classes.txt."""
    with open(classes_file, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    return classes


def create_yolo_labels(frame, output_folder, class_id, bbox):
    """Создает файл меток в формате YOLO."""
    label_filename = os.path.splitext(frame)[0] + '.txt'
    with open(os.path.join(output_folder, label_filename), 'w') as label_file:
        # bbox должен быть в формате (x_min, y_min, x_max, y_max)
        x_min, y_min, x_max, y_max = bbox
        # Нормализуем координаты
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        width = x_max - x_min
        height = y_max - y_min

        # Преобразуем в нормализованные значения
        label_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


def create_yolo_dataset(frames_folder, output_folder, classes_file, train_ratio=0.7):
    # Загружаем классы из файла
    classes = load_classes(classes_file)

    # Создаем необходимые папки
    os.makedirs(os.path.join(output_folder, 'images/train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'images/val'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels/train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'labels/val'), exist_ok=True)

    # Получаем список всех кадров
    frames = [f for f in os.listdir(frames_folder) if f.endswith('.jpg')]
    random.shuffle(frames)

    # Разделяем на train и val
    train_size = int(len(frames) * train_ratio)
    train_frames = frames[:train_size]
    val_frames = frames[train_size:]

    # Пример данных о координатах (замените на ваши данные)
    # Формат: {frame_name: [(class_id, (x_min, y_min, x_max, y_max)), ...]}
    annotations = {
        "frame_0000.jpg": [(0, (50, 50, 150, 150))],  # Пример: класс 0, bbox
        "frame_0001.jpg": [(1, (30, 30, 120, 120))],
        # Добавьте остальные аннотации для ваших кадров
    }

    # Копируем кадры и создаем метки
    for frame in train_frames:
        shutil.copy(os.path.join(frames_folder, frame), os.path.join(output_folder, 'images/train', frame))
        # Создаем метки для каждого кадра
        if frame in annotations:
            for class_id, bbox in annotations[frame]:
                create_yolo_labels(frame, os.path.join(output_folder, 'labels/train'), class_id, bbox)

        for frame in val_frames:
            shutil.copy(os.path.join(frames_folder, frame), os.path.join(output_folder, 'images/val', frame))
            # Создаем метки для валидации
            if frame in annotations:
                for class_id, bbox in annotations[frame]:
                    create_yolo_labels(frame, os.path.join(output_folder, 'labels/val'), class_id, bbox)

        # Создаем data.yaml
        data_yaml_content = f"""
        train: {os.path.join(output_folder, 'images/train')}
        val: {os.path.join(output_folder, 'images/val')}
        nc: {len(classes)}
        names: {classes}
        """
        with open(os.path.join(output_folder, 'data.yaml'), 'w') as f:
            f.write(data_yaml_content.strip())

        # Создаем notes.json с информацией о категориях
        notes_data = {
            "categories": [{"id": i, "name": cls} for i, cls in enumerate(classes)],
            "info": {
                "year": 2024,
                "version": "1.0",
                "contributor": "Label Studio"
            }
        }

        with open(os.path.join(output_folder, 'notes.json'), 'w') as f:
            json.dump(notes_data, f, indent=2)

        print("Структура данных для YOLOv8 создана.")

    # Пример использования
    frames_folder = 'output_frames'  # Папка с извлеченными кадрами
    output_folder = 'yolo_dataset'  # Папка для сохранения датасета
    classes_file = 'classes.txt'  # Путь к файлу с классами (в той же папке, что и скрипт)
    create_yolo_dataset(frames_folder, output_folder, classes_file)
