FROM python:3.11

WORKDIR /frontend

COPY requirements.txt /frontend/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /frontend/

CMD ["streamlit", "run", "app.py"]
