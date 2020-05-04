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

## Development with heroku

Install heroku from here (https://devcenter.heroku.com/articles/heroku-cli).

    heroku login
    # login with your credentials

Clone the repo from heroku.    

    heroku git:clone -a nosecount

To deploy changes, commit and push them to the master branch. 
 
    git pull heroku master
    # make changes
    git add .
    git commit -m "changes"
    # this will trigger the deployment
    git push heroku master 

## Tests

To run tests install "pytest" and run it
    
    pip3 install -U pytest
    pytest
    

## Repo in git.ffhs.ch

A mirror of the repo exists in git.ffhs.ch.
    
    git clone https://git.ffhs.ch/mathias.begert/nosecount.git
    
## Android Demo-App

A Demo Android App exists here: https://git.ffhs.ch/janik.mabboux/noseandroid
    
## License
[MIT](https://choosealicense.com/licenses/mit/)
