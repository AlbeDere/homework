import cv2
from ocr import perform_ocr
from utils import validate_license_plate, save_to_txt
from inference_sdk import InferenceHTTPClient

# Инициализация клиента
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=""
)

def crop_license_plate(image_path):
    # Загружает изображение
    image = cv2.imread(image_path)
    result = CLIENT.infer(image_path, model_id="car-licenses-2/1")
    
    if result['predictions']:
        for prediction in result['predictions']:
            center_x = int(prediction['x'])
            center_y = int(prediction['y'])
            width = int(prediction['width'])
            height = int(prediction['height'])
            confidence = prediction['confidence']
            x = center_x - (width // 2)
            y = center_y - (height // 2)

            print(f"Detected License Plate with confidence {confidence:.2f}:")
            print(f"Coordinates: (x: {x}, y: {y}, width: {width}, height: {height})")

            license_plate_crop = image[y:y + height, x:x + width]
            cropped_image_path = "cropped_license_plate.jpg"
            cv2.imwrite(cropped_image_path, license_plate_crop)
            print(f"Cropped license plate saved as '{cropped_image_path}'.")
            ocr_result = perform_ocr(cropped_image_path, confidence, image_path)
            if validate_license_plate(ocr_result['license_plate']):
                save_to_txt(ocr_result)
            return

    print("No license plate detected.")
