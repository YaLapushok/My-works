import os
import yaml
from shutil import copy2
from pathlib import Path
import random


def get_subfolder_names(directory):
    """Create classes name for learning
    Args:
        directory="path_to_folder"
    """
    subfolder_names = []
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            subfolder_names.append(item)
    return subfolder_names


def create_yolo_data_yaml(root_dir, class_names, dataset_dir="dataset"):
    """
    Generates a YOLO-style data.yaml file for the given dataset structure with organized folders.

    Args:
    - root_dir (str): Path to the root directory where sections and classes are stored.
    - class_names (list): List of class names to include in the dataset.
    - dataset_dir (str): Name of the main dataset directory (default: 'dataset').

    Returns:
    - None
    """
    
    # Normalize class names to ensure consistency (all as strings)
    class_names = [str(class_name) for class_name in class_names]

    # Initialize the structure for data.yaml
    data_yaml = {
        'train': str(Path(dataset_dir) / "images" / "train"),
        'val': str(Path(dataset_dir) / "images" / "val"),
        'nc': len(class_names),
        'names': class_names
    }

    # Prepare lists for image paths (train and validation)
    train_images = []
    val_images = []
    
    # Create directories for images and labels (if they don't exist)
    images_train_dir = Path(dataset_dir) / "images" / "train"
    images_val_dir = Path(dataset_dir) / "images" / "val"
    labels_train_dir = Path(dataset_dir) / "labels" / "train"
    labels_val_dir = Path(dataset_dir) / "labels" / "val"
    
    images_train_dir.mkdir(parents=True, exist_ok=True)
    images_val_dir.mkdir(parents=True, exist_ok=True)
    labels_train_dir.mkdir(parents=True, exist_ok=True)
    labels_val_dir.mkdir(parents=True, exist_ok=True)

    # Traverse root_dir to find and collect images for the given class names
    for section in os.listdir(root_dir):
        section_path = os.path.join(root_dir, section)
        
        # Only process directories (skip files)
        if os.path.isdir(section_path):
            for class_name in class_names:
                class_dir = os.path.join(section_path, class_name)
                
                if os.path.isdir(class_dir):
                    # Iterate over the images in the class directory
                    for img_file in os.listdir(class_dir):
                        if img_file.lower().endswith(".png"):  # Handle case-insensitive filenames
                            img_path = os.path.join(class_dir, img_file)
                            
                            # Determine if this goes into training or validation
                            if random.random() < 0.8:  # 80% for training, 20% for validation
                                train_images.append(img_path)
                                # Copy image to the train directory
                                copy2(img_path, images_train_dir / img_file)
                                
                                # Create a label for the image (YOLO format: class_index x_center y_center width height)
                                label_path = labels_train_dir / img_file.replace(".png", ".txt")
                                with open(label_path, "w") as label_file:
                                    class_index = class_names.index(class_name)  # Get the class index
                                    label_file.write(f"{class_index} 0.5 0.5 1.0 1.0\n")  # Full image bbox
                            else:
                                val_images.append(img_path)
                                # Copy image to the validation directory
                                copy2(img_path, images_val_dir / img_file)
                                
                                # Create a label for the image (YOLO format)
                                label_path = labels_val_dir / img_file.replace(".png", ".txt")
                                with open(label_path, "w") as label_file:
                                    class_index = class_names.index(class_name)  # Get the class index
                                    label_file.write(f"{class_index} 0.5 0.5 1.0 1.0\n")  # Full image bbox

    # Write data.yaml to the current directory
    with open("data.yaml", "w") as yaml_file:
        yaml.dump(data_yaml, yaml_file)

    print(f"data.yaml file created with {len(train_images)} training images and {len(val_images)} validation images.")

# Usage
root_directory = 'small_signs'
all_folders = []
for folder in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder)
    if os.path.isdir(folder_path):
        subfolders = get_subfolder_names(folder_path)
        all_folders.append(subfolders)

# Create names for classes in directory
class_names_list = []
for subfolder_list in all_folders:
    class_names_list.extend(subfolder_list)

print(class_names_list)


create_yolo_data_yaml(root_directory, class_names_list)
