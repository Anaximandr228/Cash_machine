# Тестовое задание

## Установка
Создать новое окружение `python -m venv venv`<br>
Создать базу данных PostgreSQL<br>
В файле "settings.py" внести характеристики подключения к своей базе данных PostgreSQL


### Для Windows:
>Активировать созданное окружение `cd venv/scripts` , `activate.bat` , деактивировать - выполнить `deactivate.bat`
>
>Вернуться к папке проекта `cd ../../`
### Для mac и linux:
>Активировать созданное окружение `source venv/bin/activate`, деактивировать - выполнить `deactivate`

Для установки всех зависимостей выполнить `pip install -r requirements.txt`

Для запуска выполнить:<br>
`python manage.py migrate`<br>
`python database.py`<br>
`python manage.py runserver 0.0.0.0:8000`

## Для проверки эндпоинтов:
1. Вызовите "/cash_machine" и передайте в него: {items": [1, 2]} для получения qr-кода с ссылкой
2. Вызовите "/media/..." для получения товарного чека