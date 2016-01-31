#!/usr/bin/env bash
cd frontend
npm install

# build frontend
node node_modules/webpack/bin/webpack.js

cd ..

docker build -t wasgeit . && \
    docker stop wasgeit && \
    docker rm wasgeit && \
    docker run -dp 80:8080 --name wasgeit wasgeit