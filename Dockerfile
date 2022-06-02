FROM python:3.9
WORKDIR /url_shortener

ENV FLASK_APP=app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY app ./app

CMD flask run --host=0.0.0.0
