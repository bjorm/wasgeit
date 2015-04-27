#!/usr/bin/env bash
cd frontend
npm install

# build frontend
node node_modules/webpack/bin/webpack.js

# prepare install
sudo systemctl stop httpd

# install frontend
sudo cp target/* /var/www/html/wasgeit

# install backend
cd ../backend/src
sudo cp -r *.py wasgeit.fcgi crawler /var/www/cgi-bin/wasgeit
sudo chmod +x /var/www/cgi-bin/wasgeit/wasgeit.fcgi

# start apache
sudo systemctl start httpd