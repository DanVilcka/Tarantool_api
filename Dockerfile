# Используем образ Python 3.9 как базу для нашего образа
FROM python:3.9-slim

# Устанавливаем рабочий каталог в /app
WORKDIR /app

# Установка Poetry
RUN pip install poetry

# Копируем файл pyproject.toml и poetry.lock (если есть) в рабочий каталог
COPY pyproject.toml poetry.lock ./

# Установка зависимостей с помощью Poetry
RUN poetry install --no-dev

# Копируем все файлы из текущего каталога в рабочий каталог
COPY . .

# Указываем команду для запуска приложения через Poetry
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]