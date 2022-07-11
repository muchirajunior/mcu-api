from main import app,request
from users import users
from  projects import projects

app.register_blueprint(users)
app.register_blueprint(projects)


@app.route("/")
def index():

    return {"message":"api running successfully"}



# if __name__=="__main_ _":
#     app.run(debug=True) 
