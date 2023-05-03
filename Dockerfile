FROM python:3.9.16-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./formApp ./

RUN pip uninstall django

RUN pip install -r /app/requirements.txt    

# RUN python manage.py collectstatic --no-input


# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD [ "gunicorn", "formApp.wsgi:application", "--bind", "0.0.0.0.:8000" ]