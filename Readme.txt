Ошибка tesseract is not installed or it's not in your PATH указывает на то, что Python не может найти исполняемый файл Tesseract OCR. Это может быть связано с несколькими причинами:

    Tesseract не установлен.
    Путь к Tesseract не добавлен в переменную среды PATH.
    Python не может найти Tesseract из-за неправильного пути.

Давайте рассмотрим, как решить эту проблему на разных операционных системах.
На Windows

    Убедитесь, что Tesseract установлен:
        Скачайте и установите Tesseract OCR с официального сайта или с репозитория GitHub: Tesseract OCR для Windows.
        Запустите установщик и следуйте инструкциям.

    Добавьте путь к Tesseract в переменную среды PATH:
        Нажмите Win + X и выберите Система.
        В левой панели выберите Дополнительные параметры системы.
        В окне Системные свойства нажмите Переменные среды.
        В разделе Системные переменные найдите переменную Path и нажмите Изменить.
        Нажмите Создать и добавьте путь к папке, где установлен Tesseract. Например, если Tesseract установлен в C:\Program Files\Tesseract-OCR, добавьте C:\Program Files\Tesseract-OCR.
        Нажмите ОК, чтобы сохранить изменения.

    Перезапустите командную строку или терминал.

    Проверьте установку:
        Откройте командную строку (CMD) и введите:

        tesseract --version

        Если Tesseract установлен и доступен в PATH, вы увидите версию Tesseract.

На macOS

    Установите Tesseract OCR с помощью Homebrew:
        Откройте терминал.
        Убедитесь, что Homebrew установлен. Если нет, выполните:

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

        Установите Tesseract:

        brew install tesseract

    Проверьте установку:
        В терминале введите:

        tesseract --version

        Если Tesseract установлен и доступен в PATH, вы увидите версию Tesseract.

На Linux (Ubuntu)

    Установите Tesseract OCR:
        Откройте терминал.
        Обновите список пакетов:

        sudo apt-get update

        Установите Tesseract:

        sudo apt-get install tesseract-ocr

    Проверьте установку:
        В терминале введите:

        tesseract --version

        Если Tesseract установлен и доступен в PATH, вы увидите версию Tesseract.

Проверка установки Tesseract в Python

После установки Tesseract и добавления его в PATH, вы можете проверить, что Python может его использовать, с помощью следующего кода:

import pytesseract

# Проверка версии Tesseract
print(pytesseract.get_tesseract_version())

Если Tesseract установлен и доступен, этот код выведет версию Tesseract.
Дополнительные меры

Если проблема persists, попробуйте явно указать путь к Tesseract в коде:

import pytesseract

# Укажите полный путь к tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Проверка версии Tesseract
print(pytesseract.get_tesseract_version())

Этот код явно указывает путь к исполняемому файлу Tesseract, что может помочь Python найти его. Убедитесь, что путь указан правильно и соответствует вашей установке.