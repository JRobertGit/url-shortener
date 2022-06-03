FROM python:3.9.13-slim-buster
WORKDIR /url_shortener

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app ./app

EXPOSE 5000
CMD ["flask", "run"]
