#app.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:88888888@127.0.0.1:3307/todo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

from listtodo import app_api

app.register_blueprint(app_api, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)