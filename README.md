# Blogicum

> Blogicum - это блоговая платформа на базе Django,
которая позволяет создавать и публиковать блоги. 
Она предоставляет простой и интуитивно понятный интерфейс для управления записями, 
категориями и статическими страницами.

# Установка

1. Клонируйте репозиторий на свою локальную машину:

   git clone git@github.com:SHURSHALO/django_sprint1.git

2. Перейдите в директорию проекта:

   cd django_sprint1

3. Создайте и активируйте виртуальное окружение (опционально):

   python3 -m venv venv
   source venv/Scripts/activate

4. Установите необходимые зависимости:

   pip install -r requirements.txt

5. Примените миграции базы данных:
   
   python manage.py migrate

6. Запуск python manage.py runserver

Откройте веб-браузер и перейдите по адресу http://localhost:8000/, чтобы получить доступ к приложению Blogicum.
