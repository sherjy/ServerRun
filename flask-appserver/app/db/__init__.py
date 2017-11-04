#-*- coding: UTF-8 -*- 
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db=SQLAlchemy()

#sqlite/mysql
sqlUrl="sqlite:////tmp/test.db"

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=sqlUrl
    db.init_app(app)
    return app
