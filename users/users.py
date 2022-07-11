import sys
from flask import Blueprint,request,redirect,jsonify
sys.path.append("..")
from main import db,jwt_required,uuid,create_access_token,bcrypt

users=Blueprint('users',__name__,url_prefix='/users')

@users.get("/")
@jwt_required()
def getAllUsers():
    users=db.users.find()
    users=[user for user in users]

    return jsonify(users)

@users.get("/<userId>")
@jwt_required()
def getUserById(userId):
    try:
        user=db.users.find_one({"_id":userId})
        user.pop('password')

        return jsonify(user)

    except Exception as e:
        return jsonify({"msg":"failed to load user","error":str(e)})

@users.post("/")
def createUser():
    try:
        data= request.json
        if db.users.find_one({'username':data['username']}):
            return jsonify({"msg":"failed to register user","error":"username already exists"}),406
        data['_id']=uuid()
        data['password']=bcrypt.generate_password_hash(data['password'],10).decode("utf-8") 
        db.users.insert_one(data)

        return jsonify({"msg":"created user successfully"}),200
    except Exception as e:
        return {"msg":"failed to register user","error":str(e)},406

@users.post("/login")
def loginUser():
    try:
        data=request.json
        user=db.users.find_one({'username':data['username']})
        if user == None:
            return {"msg":"login failed, username does not exist"},406
        if bcrypt.check_password_hash(user['password'].encode('utf-8'),data['password']) :
            user.pop("password")
            token=create_access_token(identity=user)
            return jsonify({"msg":"login successful","user":user,"token":token}),200

        else:
            return {"msg":"login failed, incorrect password"},406

    except Exception as e:
        return jsonify({ "msg":"login failed","error":str(e)}),406

@users.put("/<userId>")
@jwt_required()
def updateUser(userId):
    try:
        data=request.json
        db.users.update_one({'_id':userId},{"$set":data})
        user=db.users.find_one({"_id":userId})
        user.pop('password')

        return jsonify({"msg":"updated user successfully","user":user}),200

    except Exception as error:
        return jsonify({"msg":"failed to update user","error":str(error)}),406

@users.patch("/<userId>")
def updatePassword(userId):
    try:
        password=request.json['password']
        password=bcrypt.generate_password_hash(password,10).decode('utf-8')
        db.users.find_one_and_update({'_id':userId},{"$set":{"password":password}})

        return jsonify({"msg":"updated password successfully"}),200
    except Exception as error:
        return jsonify({"msg":"failed to update password","error":str(error)}),406


@users.delete("/<userId>")
@jwt_required()
def deleteUser(userId):
    try:
        user=db.users.find_one_and_delete({'_id':userId})

        return {"msg":f"user {user['name']} deleted sucessfully"},200
    except Exception as e :
        return jsonify( {"msg":"failed to delete user","error":str(e)}),406


@users.get("/<userId>/projects")
@jwt_required()
def getUserProjects(userId):
    projects=db.projects.find({"owner":userId})
    projects=[project for project in projects]

    return jsonify(projects)

@users.post("/<userId>/projects")
@jwt_required()
def createUserProject(userId):
    try:
        data=request.json
        data['_id']=uuid()
        data['owner']=userId
        db.projects.insert_one(data)

        return jsonify({"project":data,"msg":"project created successfully"}),200
    except:
        return {"msg":"failed to create project"},406

@users.patch("/<userId>/projects/<projectId>")
@jwt_required()
def updateUserProjectPin(userId, projectId):
    try:
        data=request.json
        pin=data['pin']
        project=db.projects.find_one({'_id':projectId})
        if project['owner'] != userId:
            return {"msg":"failed to update, unauthorized to update"},406

        db.projects.update_one({"_id":projectId},{"$set":{f'pins.{pin}.value':data['value'] }})
        project=db.projects.find_one({'_id':projectId})
        return jsonify({"project":project,"msg":"updated successfully"}),200
        
    except Exception as e:
        return jsonify({"msg":"failed to update project","error":str(e)}),406

@users.delete("/<userId>/projects/<projectId>")
@jwt_required()
def deleteProject(userId,projectId):
    try:
        project=db.projects.find_one({'_id':projectId})
        if project['owner'] != userId:
            return {"msg":"failed to delete, unauthorized to delete"},406
        
        db.projects.delete_one({"_id":projectId})

        return {"msg":f"project {project['name']} deleted successfully"},200
    except Exception as e:
        return jsonify({"msg":"failed to delete","error":str(e)}),406
    