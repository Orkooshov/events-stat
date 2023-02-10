# syntax=docker/dockerfile:1

FROM        python:3.10
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR     /lcn-stat-3.0
COPY        . .
CMD         ["python3", "-m", "streamlit", "run", "1_🏠_Home.py"]
EXPOSE      8501
