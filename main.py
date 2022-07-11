# type:ignore
from flask import Flask,request
from flask_pymongo import PyMongo
from shortuuid import uuid
from flask_jwt_extended import create_access_token, get_jwt_identity,jwt_required,JWTManager
from flask_bcrypt import Bcrypt
from datetime import timedelta
from flask_cors import CORS
# import os

app=Flask(__name__)

app.config['MONGO_URI']="mongodb://muchira-mongodb:vyWp23h7oJCplSzqx3CzsQqjLqp1g0rRKi38cUMX0Ul818LnuoUBlvoKP4cCqIjJljh0WWBRniThYdliRiiFEQ==@muchira-mongodb.mongo.cosmos.azure.com:10255/mcudb?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@muchira-mongodb@"
app.config["JWT_SECRET_KEY"] = "FJVDJH93623FDNJHGS537KDGN6@#$%JJ"
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(days=100)
app.config["SECRET_KEY"]="fbudue730fbsjk78bnwo"

jwt = JWTManager(app)

mongoClient=PyMongo(app)
db=mongoClient.db

bcrypt=Bcrypt(app)
CORS(app)
