FROM python:3.9

WORKDIR /app 
# создаем папку в контейнере
COPY requirements.txt /app
# создаем в контейнере файл для зависимостей
RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt
# подгружаем в файл зависимости
EXPOSE 5000
#Команда EXPOSE настраивает порт для своего сервера. 
#Это необходимо, чтобы Docker мог нужным образом настроить Сеть в контейнере. 

COPY . /app