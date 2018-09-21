Flask Vuejs Docker Starter
====================

## Development Setup

* `pipenv install`

* `pipenv shell`

* `export FLASK_APP=services && flask run`

From `client` directory using Node 8.x

* `npm install`

* `npm run serve`

Visit app at http://localhost:8080

## Build

`docker build -t flask-vuejs-docker .`

## Deploy

`docker run -p 80:8080 flask-vuejs-docker`

## Running the tests

`pipenv install --dev`

`pipenv run python -m pytest`