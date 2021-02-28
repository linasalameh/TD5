#!/bin/bash

# creation de l'env + install des deps
if [ ! -d ".env" ];then
	  python3 -m venv .env
fi

# activation de l'env
source .env/bin/activate
pip install -r requirements.txt

# start le programme
python3 main.py
