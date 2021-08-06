# i want this whole folder to be one package;
# instantiate this as my entire application

from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate
from .models import db, login_manager, ma
from .helpers import JSONEncoder
from flask_cors import CORS



# create a Flask app & pass everything in from the directory
# __name__ takes on the directory it is inside of
app = Flask(__name__)
app.config.from_object(Config)

# postgresql+psycopg2://<username>:<password>@localhost:<port>/<db_name>

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

db.init_app(app)

login_manager.init_app(app)
ma.init_app(app)

# specifies what page to load for non-authenticated users if sign-in is unsuccessful
login_manager.login_view = 'auth.signin'

migrate = Migrate(app, db)

app.json_encoder = JSONEncoder


CORS(app)

from .models import User

