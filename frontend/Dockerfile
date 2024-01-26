FROM python:3.8

WORKDIR /app

COPY ./app.py /streamlit-app/app.py

RUN pip install streamlit requests

CMD ["streamlit", "run", "app.py"]
