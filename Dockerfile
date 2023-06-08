FROM python:3-slim

WORKDIR /QACloudCamp_test

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD python -m pytest -v

