import zipfile
import os
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import torch

# Функция для распаковки ZIP-файла
def unzip_data(zip_file_path, extraction_path):
    os.makedirs(extraction_path, exist_ok=True)  # Создаем папку для извлеченных данных
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)
    print("Извлечение завершено!")

# Путь к вашему ZIP-файлу
zip_file_path = 'path/to/yourfile.zip'
extraction_path = 'path/to/extracted_data'

# Распаковываем ZIP-файл
unzip_data(zip_file_path, extraction_path)

# Задаем пути к изображениям и аннотациям
images_dir = os.path.join(extraction_path, 'images')  # Папка с изображениями
labels_dir = os.path.join(extraction_path, 'labels')  # Папка с аннотациями

# Класс для загрузки данных в формате YOLO
class YOLODataset(Dataset):
    def __init__(self, images_dir, labels_dir, transform=None):
        self.images_dir = images_dir
        self.labels_dir = labels_dir
        self.transform = transform
        self.image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        image_file = self.image_files[idx]
        image_path = os.path.join(self.images_dir, image_file)
        label_path = os.path.join(self.labels_dir, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))

        # Загружаем изображение
        image = Image.open(image_path).convert("RGB")

        # Применяем трансформации к изображению
        if self.transform:
            image = self.transform(image)

        # Загружаем аннотации и преобразуем их
        boxes = []
        labels = []
        with open(label_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                class_id = int(parts[0])
                x_center, y_center, width, height = map(float, parts[1:])
                boxes.append([x_center, y_center, width, height])
                labels.append(class_id)

        boxes = torch.tensor(boxes, dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.int64)

        return image, boxes, labels

# Трансформации для изображений
transform = transforms.Compose([
    transforms.Resize((640, 640)),
    transforms.ToTensor()
])

# Создаем датасет и загрузчик данных
dataset = YOLODataset(images_dir=images_dir, labels_dir=labels_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=8, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))

# Загружаем предобученную модель, например, YOLOv5
from ultralytics import YOLO

model = YOLO('yolov5s.pt')  # Замените на свою модель, если нужно

# Настройка и запуск обучения
model.train(data='path/to/custom_data.yaml', epochs=10, batch=8, imgsz=640)

print("Обучение завершено!")
