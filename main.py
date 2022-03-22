# type:ignore
from flask import Flask,request
from flask_pymongo import PyMongo
from shortuuid import uuid
from flask_jwt_extended import create_access_token, get_jwt_identity,jwt_required,JWTManager
from flask_bcrypt import Bcrypt
from datetime import timedelta
import os

app=Flask(__name__)

app.config['MONGO_URI']="mongodb://junior-mongo:xse7Nsg0qgsOZwI86Yoe5NX77CBhftipW8VCDd7RHFzJeRPkE4buU8lw3tbRTQs2fkROnmk21r7NQcZbg4nNlg==@junior-mongo.mongo.cosmos.azure.com:10255/mcuapi?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@junior-mongo@"
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(minutes=40)
app.config["SECRET_KEY"]=os.getenv("API_KEY")

jwt = JWTManager(app)

mongoClient=PyMongo(app)
db=mongoClient.db

bcrypt=Bcrypt(app)