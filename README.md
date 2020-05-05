# Nosecount

Nosecount is a webservice for counting people in an image.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nosecount service.

```bash
git clone {this_repo}
cd nosecount
pip3 install -r requirements.txt
```

## Usage

Start the gunicorn webserver and go to http://localhost:8000
```bash
gunicorn app:app
```
For the API-docs visit http://localhost:8000/apidocs

## Demo

The service is hosted as a heroku application at:

https://nosecount.herokuapp.com/apidocs

A push to the master branch will trigger CI on github, on success it will deploy the changes.

## Tests

To run tests, install "pytest" and run it. An instance of the application must be running on localhost:8000.
    
    pip3 install -r requirements-test.txt
    pip3 install -U pytest
    pytest


## Android Demo-App

A Demo Android App exists here: https://git.ffhs.ch/janik.mabboux/noseandroid
    
## License
[MIT](https://choosealicense.com/licenses/mit/)
