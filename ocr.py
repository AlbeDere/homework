import cv2
import pytesseract
import re
from utils import correct_license_plate_format

def perform_ocr(cropped_image_path, confidence, image_id):
    # Загружает обрезанное изображение и выполняет OCR
    img = cv2.imread(cropped_image_path)
    custom_config = r'--oem 3 --psm 8'
    text = pytesseract.image_to_string(img, config=custom_config)
    print("OCR Result:")
    cleaned_text = clean_license_plate(text)
    print(cleaned_text)
    return {'image_id': image_id, 'license_plate': cleaned_text, 'confidence': confidence}

def clean_license_plate(text):
    # Убирает не алфавитные символы и приводит к верхнему регистру
    cleaned_text = re.sub(r'[^A-Z0-9]', '', text.upper()).strip()
    if len(cleaned_text) > 6:
        cleaned_text = cleaned_text[-6:]
    cleaned_text = correct_license_plate_format(cleaned_text)  # Корректирует формат номерного знака
    return cleaned_text
