# type:ignore
from flask import Flask
from flask_pymongo import PyMongo
from shortuuid import uuid

app=Flask(__name__)

app.config['MONGO_URI']="mongodb://127.0.0.1:27017/mcuapi"

mongoClient=PyMongo(app)
db=mongoClient.db