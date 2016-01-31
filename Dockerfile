FROM debian:jessie
#USER nobody
#WORKDIR

RUN apt-get update && apt-get install -y nginx python3 python3-pip gcc libxml2-dev libxslt-dev zlib1g-dev

RUN pip3 install virtualenv

RUN mkdir -p /var/www/wasgeit/backend && \
    cd /var/www/wasgeit/backend && \
    virtualenv python3-wasgeit && \
    . python3-wasgeit/bin/activate && \
    pip install flask pyquery feedparser uwsgi

COPY ../backend /var/www/wasgeit/backend

COPY wasgeit_nginx.conf /var/www/wasgeit
COPY uwsgi_params /var/www/wasgeit/backend

RUN ln -s /var/www/wasgeit/wasgeit_nginx.conf /etc/nginx/conf.d/

CMD nginx
EXPOSE 8080