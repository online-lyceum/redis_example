FROM python:3.11
WORKDIR /app
RUN pip3 install redis

COPY hello.py ./
CMD python3 hello.py

