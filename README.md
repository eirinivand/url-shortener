# url-shortener
follow these steps
http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/
specifically the steps about python, pip install, pip install virtualenv, mkvirtualenv urlenv,

if you have already created a virtual environment then go to that directory under Scripts open a cmd and run: activate

download the dist folder and all it's components from GitHub project and while in virtual
environment go to where you saved the dist folder and run the following commands

command 1: pip install url_shortener-1.1.0-py3-none-any.whl

command 2:set FLASK_APP=url_shortener

command 3:flask init-db

command 4:flask load-db

command 5:flask run

you are now running the application.
go to http://127.0.0.1:5000/format/formatter to shorten a URL
