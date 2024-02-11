FROM python:3.10

WORKDIR /frontend

COPY . /frontend

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app.py"]
