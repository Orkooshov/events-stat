# syntax=docker/dockerfile:1

FROM        python:3.12.0a5
WORKDIR     /lcn-stat-3.0
COPY        . .
RUN         python -m pip install -r requirements.txt
CMD         ["python", "-m", "-streamlit", "run", "1_🏠_Home.py"]
EXPOSE      8501
