from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = '3d951e864422a3d0fc27b496b06a5c9f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localHost:5432/Otvoreno_racunarstvo"
app.config['PATH'] = os.path.abspath('..').replace('\\', '/')
app.config['AUTH0_CLIENT_ID'] = '0F6lPPCGlAimdbq03B1MyPKROlDVFj1i'
app.config['AUTH0_CLIENT_SECRET'] = '5Nvyjy5NgCdG5SWSZa6VWRgPi8_pX3QQ38pngOg7Z5v1UACAcqODfa5T0WtMoyaX '
app.config['AUTH0_DOMAIN'] = 'dev-8nfqfpbzo0kif14w.us.auth0.com'
db = SQLAlchemy(app)

from otvoreno_racunarstvo import routes