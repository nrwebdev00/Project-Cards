from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SECRET_KEY'] = 'dev'

if __name__ == "__main__":
    app.run(debug = True)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
