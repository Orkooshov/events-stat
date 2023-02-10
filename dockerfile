# syntax=docker/dockerfile:1

FROM        python:3.10
WORKDIR     /lcn-stat-3.0
COPY        . .
RUN         python3 -m venv venv
ENV         PATH=venv/bin:$PATH
RUN         python3 -m pip install pip --upgrade \
RUN         python3 -m pip install -r requirements.txt
CMD         ["python3", "-m", "-streamlit", "run", "1_🏠_Home.py"]
EXPOSE      8501
