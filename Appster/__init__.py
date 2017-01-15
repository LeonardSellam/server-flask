from flask import Flask
from .client.admin import admin
from .database import init_db
from .database import db_session
from flask_login import LoginManager
from .models.users import User


app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(admin, url_prefix='/admin')

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')

login_manager = LoginManager()

login_manager.init_app(app)


init_db()
