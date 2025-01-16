import cv2
import os

def convert_video_to_grayscale(input_video_path, output_video_path):
    if not os.path.exists(input_video_path):
        print(f"Ошибка: Входной файл '{input_video_path}' не найден.")
        return

    # Открываем видеофайл
    cap = cv2.VideoCapture(input_video_path)

    # Получаем параметры видео
    fps = cap.get(cv2.CAP_PROP_FPS)  # Частота кадров
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Ширина
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Высота

    # Создаем объект для записи видео
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Кодек для сохранения видео
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), isColor=False)

    while True:
        # Читаем кадр
        ret, frame = cap.read()
        if not ret:
            break  # Если кадры закончились, выходим из цикла

        # Преобразуем кадр в черно-белый формат
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Записываем черно-белый кадр в выходное видео
        out.write(gray_frame)

    # Освобождаем ресурсы
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Пример использования
input_video = 'А-180_ст_нап_Черемыкино/А-180_ст_нап_Черемыкино_км52+650-км56+700.avi'  # Путь к входному видеофайлу (AVI)
output_video = 'А-180_ст_нап_Черемыкино1.avi'  # Путь к выходному видеофайлу (AVI)
convert_video_to_grayscale(input_video, output_video)
