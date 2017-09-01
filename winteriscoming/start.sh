#!/bin/bash

screen -dmS winteriscoming1 bash -c 'python3 -m http.server 41001'
screen -dmS winteriscoming2 bash -c 'python3 -m http.server 41002'
screen -dmS winteriscoming3 bash -c 'python3 -m http.server 41003'
screen -dmS winteriscoming4 bash -c 'python3 -m http.server 41004'
