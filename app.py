from main import app
from users import users
from  projects import projects

app.register_blueprint(users)
app.register_blueprint(projects)


@app.route("/")
def index():

    return {"message":"app running successfully"}


# if __name__=="__main_ _":
#     app.run(debug=True) 