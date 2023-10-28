import datetime
import os

import segno

# $ poetry run python scripts/generate_qr.py

# Получите текущую дату и время
current_datetime = datetime.datetime.now()

# Форматируйте дату и время в строку
formatted_date = current_datetime.strftime("%Y-%m-%d_%H-%M")  # Например, "2023-10-28_14-30"

# Создайте имя папки с текущей датой
folder_name = formatted_date

# Получите текущий путь к директории, где находится ваш скрипт
current_directory = os.path.dirname(os.path.abspath(__file__))

# Создайте полный путь к новой папке
new_folder_path = os.path.join('C:\\for_git\\qr_conveyor\\data', folder_name)

# Проверьте, существует ли папка, и создайте её, если она не существует
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# Создание qr-кода и добавление его в созданную папку
qrcode = segno.make_qr("Hello, World")
qrcode.save(f"{new_folder_path}\\basic_qrcode.png")
