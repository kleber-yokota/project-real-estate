FROM apache/superset:pr-23216

COPY requirements.txt .
RUN  pip install -r requirements.txt
COPY init.sh .
COPY bootstrap.sh .
ENTRYPOINT sh init.sh
