FROM python:3.9-slim

COPY . /home/homss5-vision2-api-server
WORKDIR /home/homss5-vision2-api-server

COPY ./requirements.txt /home/homss5-vision2-api-server/requirements.txt

RUN apt-get update
RUN pip install -r requirements.txt

CMD ["python","main.py"]