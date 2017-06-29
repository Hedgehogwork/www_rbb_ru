#!/bin/sh
apt-get install -qy python-pip python-dev
pip install pip -U
pip install -r /home/vagrant/www_rbb_ru/backend/requirements.txt
