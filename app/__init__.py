from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config.from_object(Config)
#app.config['SECRET_KEY'] = 'bruh y tf os.environ not working'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app import views