# type:ignore
import sys
from flask import Blueprint
sys.path.append("..")
from main import db,jwt_required,uuid

users=Blueprint('users',__name__,url_prefix='/users')

@users.get("/")
def getAllUsers():

    return "all users"

@users.get("/<userId>")
def getUserById(userId):

    return f"get user {userId} "


