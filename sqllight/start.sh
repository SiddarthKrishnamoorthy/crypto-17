#!/bin/bash

screen -dmS sqllight1 bash -c 'FLASK_APP=server.py flask run --port 50000'
screen -dmS sqllight2 bash -c 'FLASK_APP=server.py flask run --port 50001'
screen -dmS sqllight3 bash -c 'FLASK_APP=server.py flask run --port 50002'
screen -dmS sqllight4 bash -c 'FLASK_APP=server.py flask run --port 50003'
