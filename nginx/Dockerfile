FROM nginx:1.20-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
# загружаем nginx.conf

RUN mkdir -p /home/web/default 
# создаем корневую папку для этого web-приложения 