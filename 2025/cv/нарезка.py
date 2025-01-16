import cv2
import os
import zipfile

def create_dataset_from_video(video_path, output_dir, num_images=20, frame_interval=120):
    # Проверка наличия видеофайла
    if not os.path.exists(video_path):
        print(f"Видео файл '{video_path}' не найден.")
        return

    # Создаем директорию для временных изображений, очищаем, если есть остатки
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, file))
    else:
        os.makedirs(output_dir)

    # Открываем видеофайл
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Общее количество кадров
    images = []

    # Перемещаемся к последнему кадру
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count - 1)

    # Сохраняем каждый 120-й кадр, начиная с конца
    for i in range(num_images):
        # Перемещаемся к нужному кадру
        frame_position = frame_count - 1 - i * frame_interval
        if frame_position < 0:
            break  # Если достигли начала видео, выходим из цикла

        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_position)
        ret, frame = cap.read()

        # Проверяем, успешно ли прочитан кадр
        if not ret:
            break

        # Разворачиваем кадр (по горизонтали)
        frame = cv2.flip(frame, 1)  # 1 - отражение по горизонтали

        # Сохраняем кадр
        image_path = os.path.join(output_dir, f"frame_{i}.jpg")
        if cv2.imwrite(image_path, frame):
            images.append(image_path)
        else:
            print(f"Не удалось сохранить изображение {image_path}")

    # Освобождаем видеофайл
    cap.release()

    # Проверка, что есть изображения для создания ZIP-файлов
    if len(images) == 0:
        print("Не удалось извлечь изображения из видео.")
        return

    # Создаем два ZIP-файла
    zip_files = ['11.zip', '22.zip']
    images_per_zip = len(images) // len(zip_files)

    for zip_file_name in zip_files:
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            for img_path in images[:images_per_zip]:
                zipf.write(img_path, os.path.basename(img_path))
            images = images[images_per_zip:]  # Удаляем добавленные изображения из списка

        print(f"Создан ZIP-файл: {zip_file_name}")

    # Удаляем временные изображения
    for img_path in images:
        os.remove(img_path)
    print("Процесс завершен.")

# Пример использования
video_path = 'DJI_0955.MP4'  # Укажите путь к вашему видеофайлу
output_dir = 'double_temp'  # Директория для временных изображений

create_dataset_from_video(video_path, output_dir, num_images=20, frame_interval=120)
