from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d951e864422a3d0fc27b496b06a5c9f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localHost:5432/Otvoreno_racunarstvo"
app.config['PATH'] = os.path.abspath('..').replace('\\', '/')
db = SQLAlchemy(app)

from otvoreno_racunarstvo import routes