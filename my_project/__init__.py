from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb1d488376f914f922df982974fb95a6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:/MSC/MSC SEM 2/RM/colorize-image-main/colorize-image-main/my_project/site.db'
try:
    db = SQLAlchemy(app)
    print("databaseeeeeeeeeeeeeeeeeeeee",db)
except sqlite3.Error as e:
    print(e)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from my_project import routes
