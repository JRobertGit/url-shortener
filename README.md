# URL Shortener Test (Solution)
The aplication is currently deployed on AWS [here](https://url-shortener.67m0udk2mli12.us-east-1.cs.amazonlightsail.com/). Please read the documentation for usage.
## Requirements & Development Setup

- Python 3.9
```bash
brew install python
```
- SQLite
```bash
brew install sqlite
```

Using `python 3.9`
```bash
python3 -m venv venv
source venv/bin/activate
# inside venv
(venv) pip install -r requirements.txt
```

## Tests and DEV Start up
To run functional and unit tests, and get code coverage check run:
```bash
# inside venv
(venv) python -m pytest --cov=app
```

![coverage](./images/coverage.png)

To run the project on localhost:
```bash
# inside venv
(venv) export FLASK_APP=app
(venv) export FLASK_ENV=development
(venv) flask run
```
This will start the application over [127.0.0.1:5000/](127.0.0.1:5000/)

![flask_run](./images/flask_run.png)

# API Usage
URL Shortener API supports the following routes and operations:
```
GET     localhost:5000/
GET     localhost:5000/<route>
POST    localhost:5000/api/shortener
GET     localhost:5000/api/shortener/<shortcode>
```

# Run as Container
The docker file to create the image to run the app as a container is straight forward. It adds some automation to the set up, and takes care of the dependencies, requirements and environment.
```Dockerfile
FROM python:3.9.13-slim-buster
WORKDIR /url_shortener

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app ./app

EXPOSE 5000
CMD ["flask", "run"]
```
To run using `docker`:
```bash
# to generate the image
docker build .
# to run the generated image
docker run -d -p 5000:5000 --name url_shortener <image_sha>
```
# Design
The application was design taking into consideration the low complexity requirements. Many sugar coated and more complex libraries were not used (like `Flask-RESTful`) to keep the application simple.

The application is a simple `Flask API`. So the project is structured according to that. On `./app/controllers` we'll find API related controllers that define the aplication's enpoints that use templates.
