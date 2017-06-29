#!/bin/bash
virtualenv /home/vagrant/venv
source /home/vagrant/venv/bin/activate
pip install -r /home/vagrant/www_rbb_ru/backend/requirements.txt
