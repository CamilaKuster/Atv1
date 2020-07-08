from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
FLASK_APP = app
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default

if __name__ == '__main__':
    manager.run()