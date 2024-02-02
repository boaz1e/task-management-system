FROM python:3.11

WORKDIR /backend

COPY . /backend

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysql-connector-python

ENV DB_USER=root

ENV DB_PASSWORD=12345

ENV DB_HOST=127.0.0.1

ENV DB_PORT=3306

ENV DB_NAME=task-management-db

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]