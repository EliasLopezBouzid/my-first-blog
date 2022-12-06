# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
COPY . .
RUN pip3 install -r requirements.txt
RUN DJANGO_SUPERUSER_PASSWORD=12345 python manage.py createsuperuser --noinput --username admin --email e.lopezbouzid@gmail.com
CMD [ "python", "manage.py" , "runserver" , "0.0.0.0:8000"]