# Пример Веб Приложения

С использованием технологий:

- Docker
- Compose
- Flask
- Gunicorn
- PostgreSQL
- pgamin
- nginx (reverse proxy)

# Билд

sudo docker compose -f docker-compose.yml build

# Запуск

sudo docker compose -f docker-compose.yml up

# Запуск в фоне

sudo docker compose -f docker-compose.yml up -d

browser localhost

browser localhost/pg/

# работа с командами web-приложения

sudo docker web_flask --version

sudo docker exec web_flask flask command

# Commands:

# create_db

# say_my_name

# команды в web-приложении(flask):

sudo docker exec web_flask flask command say_my_name

# say_my_name Noname

sudo docker exec web_flask flask command say_my_name -name Bob

# say_my_name Bob

sudo docker exec web_flask flask command create_db

# создание базы данных

sudo docker exec web_flask flask command create_tab

# создание таблицы

sudo docker exec web_flask flask command create_song

# заполнение таблиц артистов

sudo docker exec web_flask flask command create_item

# заполнение таблиц инвентаризации

sudo docker exec web_flask flask command create_book

# заполнение таблиц книг

sudo docker exec web_flask flask command create_super

# заполнение таблицы супермаркета

sudo docker exec web_flask flask command create_clinic

# заполнение таблицы клиники

http://127.0.0.1/add_random (routes.py)

# добавить данные в таблицу DB

https://www.youtube.com/watch?v=leUbqB2A1HI

# blueprint

sudo docker-compose -f docker-compose.yml stop

# Остановка

requirements.txt нужно добавить следующее:

flask
flask-sqlalchemy
psycopg2-binary
gunicorn

P.S. база данных и приложение пробрасываются на хост! На деве - это норм, на проде - нужно спрятать внутрь!
