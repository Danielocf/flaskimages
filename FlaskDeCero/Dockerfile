FROM python:3.10-slim-buster

WORKDIR /app

COPY FlaskDeCero/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

WORKDIR /app/FlaskDeCero


ENTRYPOINT [ "python3", "/app/FlaskDeCero/entry_point.py"]