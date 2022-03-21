# type:ignore
from flask import Blueprint
import sys
sys.path.append("..")
from main import db

projects=Blueprint('projects',__name__,url_prefix='/projects')

@projects.get("/")
def getAllProjects():

    return "all projects"

@projects.get("/<projectId>")
def getProjectById(projectId):

    return f"project id {projectId}"

@projects.post("/")
def createProject():

    return "project created"

@projects.put("/<projectId>")
def updateProject(projectId):

    return f"project {projectId} updated successfully"

@projects.delete("/<projectId>")
def deleteProject(projectId):

    return f"project {projectId} deleted successfully"
