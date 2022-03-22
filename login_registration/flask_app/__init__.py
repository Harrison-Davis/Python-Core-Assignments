from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "secretkey"

bcrypt = Bcrypt(app)

DATABASE = 'login_users_db'
