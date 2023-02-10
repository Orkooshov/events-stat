#!/bin/bash

cd /home/admn/Desktop/lcn-stat-3.0
source venv/bin/activate
python3 -m pip install pip --upgrade
python3 -m pip install -r requirements.txt
streamlit run 1_🏠_Home.py
