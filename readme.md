
# Автоматическое распознавание номерных знаков (ALPR)

Этот проект реализует систему автоматического распознавания номерных знаков (ALPR) с использованием технологий компьютерного зрения и оптического распознавания символов (OCR).

## Возможности
- Обнаружение номерных знаков на изображениях из указанной директории.
- Вырезка изображений номерных знаков.
- Выполнение OCR для извлечения символов.
- Валидация формата извлеченных номерных знаков.
- Сохранение действительных результатов в текстовый файл.

## Используемые технологии
- **Python**: Язык программирования проекта.
- **OpenCV**: Библиотека для компьютерного зрения.
- **Pytesseract**: Обертка Python для Tesseract-OCR.
- **Roboflow**: Используется для обнаружения номерных знаков.
- **Регулярные выражения**: Для очистки и валидации формата номерных знаков.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/albedere/homework.git
   cd homework
   ```

2. Создайте виртуальное окружение (по желанию):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # На Windows используйте .venv\Scripts\activate
   ```

3. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt
   ```

## Использование
1. Поместите изображения в директорию `cars`.
2. Запустите основной скрипт:
   ```bash
   python main.py
   ```

3. Результаты будут сохранены в `license_plate_results.txt`.


