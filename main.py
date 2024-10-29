from lpr import crop_license_plate
import os

def process_directory(directory):
    # Обходит все файлы в заданной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверяет, является ли файл изображением
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image_path = os.path.join(root, file)
                print(f"Processing: {image_path}")
                crop_license_plate(image_path)

if __name__ == "__main__":
    process_directory("cars")
