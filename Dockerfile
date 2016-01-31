FROM debian:jessie
#USER nobody
#WORKDIR

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY docker/locale.gen /etc/

RUN apt-get update && apt-get install -y nginx python3 python3-pip gcc libxml2-dev libxslt-dev zlib1g-dev locales

RUN pip3 install flask pyquery feedparser uwsgi

RUN mkdir -p /var/www/wasgeit/backend

COPY backend/src /var/www/wasgeit/backend

COPY frontend/target /var/www/wasgeit/static

COPY docker /var/www/wasgeit

RUN chmod +x /var/www/wasgeit/start.sh

RUN ln -s /var/www/wasgeit/wasgeit_nginx.conf /etc/nginx/conf.d/

#RUN echo "daemon off;" >> /etc/nginx/nginx.conf

EXPOSE 8080
CMD ["/var/www/wasgeit/start.sh"]
