#!/bin/bash

# run server
pip install -r requirements.txt
cd src
python manage.py runserver 0.0.0.0:8000 --insecure
