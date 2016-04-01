#!/usr/bin/env bash
set -e # stop script on errors
set -u # fail on unresolved variables

cd frontend
npm install

# build frontend
node node_modules/webpack/bin/webpack.js

cd ..

docker build -t wasgeit . && \
    docker stop wasgeit && \
    docker rm wasgeit && \
    docker run -dp 80:8080 --name wasgeit -e WASGEIT_ACCESS_TOKEN=${WASGEIT_ACCESS_TOKEN} wasgeit