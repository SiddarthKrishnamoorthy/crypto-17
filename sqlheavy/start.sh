#!/bin/bash

screen -dmS sqlheavy1 bash -c 'FLASK_APP=server.py flask run --port 40000'
screen -dmS sqlheavy2 bash -c 'FLASK_APP=server.py flask run --port 40001'
screen -dmS sqlheavy3 bash -c 'FLASK_APP=server.py flask run --port 40002'
screen -dmS sqlheavy4 bash -c 'FLASK_APP=server.py flask run --port 40003'
