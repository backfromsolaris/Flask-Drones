# imports operating system to give us file directory
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# gives access to the project in ANY OS we find ourselves in
# allows outside files/folders to be added so to the project from
# the base directory.
# "hey, this is where my file is in my computer"
#  - done every time we make a Flask application.



class Config:
    """
    Set configuration variables for our Flask app here
    Eventually will use hidden variable items - but for now, we'll leave them exposed in config
    """
    SECRET_KEY = "Gandalf the Grey"
    DEPLOY_DATABASE_URL = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Decreases unnecessary output in terminal