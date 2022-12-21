FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin --email admin@localhost --noinput
RUN python manage.py setpassword admin admin

CMD ["gunicorn","-b","0.0.0.0:80","garryarts.wsgi"]