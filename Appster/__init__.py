from flask import Flask
from .admin.admin import admin


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(admin, url_prefix='/admin')

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')
