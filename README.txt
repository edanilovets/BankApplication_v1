Установка проекта на Linux/Mac OS

Установка пакетов зависимостей
1) pip install -r requirements.txt

Настройка переменной окружения для Flask
2) export FLASK_APP=/<path_to_app.py_in_project_root_folder>/app.py

Инициализация приложения и создание миграции
3) flask db init
4) flask db migrate -m "initial migration"
5) flask db upgrade

Загрузка тестовых данных в базу
6) python populate_db.py

Запуск приложения
7) python app.py