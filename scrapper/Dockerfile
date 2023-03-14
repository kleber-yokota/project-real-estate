FROM python:3.11.2

USER root
RUN mkdir -p /app/driver && \
    mkdir -p /app/data

COPY ./app /app

RUN pip install -r /app/requirements.txt

CMD python /app/main.py
