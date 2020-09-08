# Small flask project from the article I wrote about deploying a flask app to an Elastic Beanstalk environment

### Installation

1. Clone the repository
2. Install virtualenv from pip
```
$ pip install virtualenv
```
2. Create a virtual environment in the folder project (actually anywhere you want)
```
$ virtualenv yourEnv
```
3. Activate your virtual environment 
```
$ source yourEnv/bin/activate
```
3. Install the required dependencies from "requirements.txt" using the following command
```
$ pip install -r requirements.txt 
```
4. Export the following environment variables
```
$ export FLASK_APP="application.py"
$ export FLASK_PORT=PORT
$ export FLASK_DEBUG=1
```
5. Run a flask dev server from the project directory
```
$ python -m flask run
```
   
