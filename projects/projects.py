from flask import Blueprint,request,jsonify,redirect
import sys
sys.path.append("..")
from main import db,uuid
from .auth import authorization

projects=Blueprint('projects',__name__,url_prefix='/projects')

@projects.get("/")
@authorization
def getAllProjects():
    data=db.projects.find()
    data=[p for p in data]

    return jsonify(data)

@projects.get("/<projectId>")
@authorization
def getProjectById(projectId):
    try:
        project=db.projects.find_one({"_id":projectId})

        return jsonify(project),200
    except:
        return {"msg":"project does not exist"}

@projects.post("/")
@authorization
def createProject():
    try:
        data=request.json
        data['_id']=uuid()
        db.projects.insert_one(data)

        return jsonify({"project":data,"msg":"project created successfully"}),200
    except:
        return {"msg":"failed to create project"},406

@projects.put("/<projectId>")
@authorization
def updateProject(projectId):
    try:
        data=request.json
        db.projects.find_one_and_replace({"_id":projectId},data)
        project=projects.find_one({"_id":projectId})
    
        return jsonify(project)
        # return redirect (f"/projects/{projectId}")
    except:
        return {"msg":"failed to update"},406

@projects.patch("/<projectId>")
@authorization
def updateProjectPin(projectId):
    try:
        data=request.json
        pin=data['pin']
        db.projects.find_one_and_update({"_id":projectId},{"$set":{f'pins.{pin}.value':data['value'] }})

        # return jsonify({"project":project,"msg":"updated successfully"}),200
        return redirect (f"/projects/{projectId}")
    except:
        return {"msg":"failed to update project"},406

@projects.delete("/<projectId>")
@authorization
def deleteProject(projectId):
    try:
        project=db.projects.find_one_and_delete({"_id":projectId})

        return {"msg":f"project {project['name']} deleted successfully"},200
    except:
        return {"msg":"failed to delete"},406
    