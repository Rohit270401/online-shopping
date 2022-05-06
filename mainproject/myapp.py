from flask import *
from new import addEmp, selectAllEmp, deleteEmp, updateEmp
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/reg")
def sign_up():
    return render_template("signup.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/emplistt")
def emp_list():
    el = selectAllEmp()
    return render_template("employeelist.html",elist=el)
    
@app.route("/addEmp" , methods=["POST"])
def add_emp():
    ide = request.form["id"]
    name = request.form["name"]
    contact = request.form["contact"]
    email = request.form["email"]
    paasw = request.form["paasw"]
    t = (ide,name,contact,email,paasw)
    addEmp(t)
    return redirect("/")

@app.route("/deleteEmp" , methods=["POST"])
def del_emp():
    ide = request.form["id"]
    t = (ide)
    deleteEmp(t)

    return redirect("/emplist")

@app.route("/updateEmp", methods=["POST"])
def update_emp():
    ide = request.form["id"]
    name = request.form["name"]
    contact = request.form["contact"]
    email = request.form["email"]
    paasw = request.form["paasw"]
    t = (name,contact,email,paasw,ide)
    updateEmp(t)
    
    return redirect("/employeelist")


if (__name__=="__main__"):
    app.run()
