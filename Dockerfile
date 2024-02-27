# Установка базового образа Windows с Python 3.7.2
FROM mcr.microsoft.com/windows-cssc/python3.7.2windows:ltsc2019

# Копирование файлов Python-скрипта в контейнер
COPY . /app

# Установка рабочей директории
WORKDIR /app

# Запуск Python-скрипта при запуске контейнера
CMD ["python", "game_with_bot.py"]
