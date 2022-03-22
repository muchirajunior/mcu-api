# type:ignore
from flask import Flask,request
from flask_pymongo import PyMongo
from shortuuid import uuid
from flask_jwt_extended import create_access_token, get_jwt_identity,jwt_required,JWTManager
from flask_bcrypt import Bcrypt
from datetime import timedelta
import os

app=Flask(__name__)

app.config['MONGO_URI']=os.getenv("DATABASE_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(minutes=40)
app.config["SECRET_KEY"]=os.getenv("API_KEY")

jwt = JWTManager(app)

mongoClient=PyMongo(app)
db=mongoClient.db

bcrypt=Bcrypt(app)