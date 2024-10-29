def validate_license_plate(plate):
    # Проверяет, что номерной знак состоит из 6 символов: первые 3 - буквы, последние 3 - цифры
    if len(plate) == 6 and plate[:3].isalpha() and plate[3:].isdigit():
        return True
    return False

def save_to_txt(result):
    # Сохраняет результаты распознавания в текстовый файл
    with open('license_plate_results.txt', mode='a') as file:
        file.write(f"Image ID/URL: {result['image_id']}, License Plate: {result['license_plate']}, Confidence: {result['confidence']:.2f}\n")

def correct_license_plate_format(plate):
    # Словари для коррекции ошибок OCR
    dict_char_to_int = {'O': '0', 'I': '1', 'J': '3', 'A': '4', 'G': '6', 'S': '5'}
    dict_int_to_char = {'0': 'O', '1': 'I', '3': 'J', '4': 'A', '6': 'G', '5': 'S'}

    first_part = plate[:3]
    second_part = plate[3:]

    # Коррекция первой части номера
    for i in range(len(first_part)):
        if first_part[i] in dict_int_to_char:
            first_part = first_part[:i] + dict_int_to_char[first_part[i]] + first_part[i + 1:]

    # Коррекция второй части номера
    for i in range(len(second_part)):
        if second_part[i] in dict_char_to_int:
            second_part = second_part[:i] + dict_char_to_int[second_part[i]] + second_part[i + 1:]

    return first_part + second_part
