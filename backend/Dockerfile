FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh /usr/wait-for-it.sh
RUN chmod +x /usr/wait-for-it.sh

COPY . /app/

CMD ["sh", "-c", "/usr/wait-for-it.sh mysql-db:3306 -- uvicorn main:app --reload --host 0.0.0.0"]
