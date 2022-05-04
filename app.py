from main import app,request
from users import users
from  projects import projects

app.register_blueprint(users)
app.register_blueprint(projects)


@app.route("/")
def index():

    return {"message":"api running successfully"}

@app.route('/ussd', methods=['POST','GET'])
def index():
    if request.method=="POST":
        data = request.data.decode('utf-8')
        return data+" junior"
    return "message from muchira junior "


# if __name__=="__main_ _":
#     app.run(debug=True) 