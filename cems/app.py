from flask import Flask, request,render_template,redirect,url_for,jsonify,flash

app = Flask(__name__)


higher_credentials={"100":{"password":"police@123"},
                    "101":{"password":"swaroop@123"},
                    "581":{"Name":"swaroop","password":"swaroop@123","Email":"swaroopedupulapati1@gmail.com","phone_no":"9999999999","Address":"marlapadu","Qualification":"btech"}}
lower_credentials={"10":{"password":"tiru@123"},
                   "11":{"password":"ashok@123"},
                    "581":{"Name":"swaroop","password":"swaroop@123","Email":"swaroopedupulapati1@gmail.com","phone_no":"9999999999","Address":"marlapadu","Qualification":"btech"}}

higher_id=""
lower_id=""


@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('login.html')

@app.route('/higher_login',methods=['GET', 'POST'])
def higher_login():
    global higher_credentials
    id=request.form['id']
    global higher_id
    higher_id=id
    password=request.form['password']
    if (id in higher_credentials) and (password == higher_credentials[id]["password"]) :
        print(higher_credentials[id])
        return render_template('higher_home.html')
    else:
        return render_template("login.html",msg="invalid credentials")
@app.route('/lower_login',methods=['GET', 'POST'])
def lower_login():
    global lower_credentials
    id=request.form['id']
    global lower_id
    lower_id=id
    password=request.form['password']
    if (id in lower_credentials) and (password == lower_credentials[id]["password"]):
        print(lower_credentials[id])
        return render_template('lower_home.html')
    else:
        return render_template("login.html",msg="invalid credentials")


@app.route('/viewhipro',methods=['GET', 'POST'])
def viewhipro():
    global higher_credentials
    global higher_id
    data=higher_credentials[higher_id]
    return render_template("view_hip.html",profile=data)

@app.route('/viewlopro',methods=['GET', 'POST'])
def viewlopro():
    global lower_credentials
    global lower_id
    data=lower_credentials[lower_id]
    return render_template("view_lop.html",profile=data)

@app.route('/viewcase',methods=['GET', 'POST'])
def viewcase():
    pass

@app.route('/entercase',methods=['GET', 'POST'])
def entercase():
    pass

@app.route('/removecase',methods=['GET', 'POST'])
def removecase():
    pass

@app.route('/reghio',methods=['GET', 'POST'])
def reghio():
    if request.method == 'POST':
        global higher_credentials
        ID=request.form['id']
        Name=request.form['name']
        Password=f"{ID}@123"
        Email=request.form["email"]
        Phone=request.form["phone"]
        Address=request.form["address"]
        Qualification=request.form["qualification"]
        if ID not in higher_credentials:
            higher_credentials[ID]={"Name":Name,"password":Password,"Email":Email,"phone_no":Phone,"Address":Address,"Qualification":Qualification}
            print(higher_credentials[ID])
            return f"{Name} updated successfully"
        else:
            return render_template("register_hio.html")
    else:
        return render_template("register_hio.html")

@app.route('/regloo',methods=['GET', 'POST'])
def regloo():
    if request.method == 'POST':
        global lower_credentials
        ID=request.form['id']
        Name=request.form['name']
        Password=f"{ID}@123"
        Email=request.form["email"]
        Phone=request.form["phone"]
        Address=request.form["address"]
        Qualification=request.form["qualification"]
        if ID not in lower_credentials:
            lower_credentials[ID]={"Name":Name,"password":Password,"Email":Email,"phone_no":Phone,"Address":Address,"Qualification":Qualification}
            print(lower_credentials[ID])
            return f"{Name} updated successfully"
        else:
            return render_template("register_loo.html")
    else:
        return render_template("register_loo.html")

@app.route('/remhio',methods=['GET', 'POST'])
def remhio():
    pass

@app.route('/remloo',methods=['GET', 'POST'])
def remloo():
    pass

@app.route('/hio_changepasss',methods=['GET', 'POST'])
def hio_changepasss():
    global higher_credentials
    if request.method == 'POST':
        op=request.form['op']
        np=request.form['np']
        if op==higher_credentials[higher_id]["password"]:
            higher_credentials[higher_id]["password"]=np
            return"""
                    <h1>password change successfully</h1>    """
        else:
            return render_template("change_hio_pass.html")
    else:
        return render_template("change_hio_pass.html")


@app.route('/loo_changepasss',methods=['GET', 'POST'])
def loo_changepasss():
    global lower_credentials
    if request.method == 'POST':
        op=request.form['op']
        np=request.form['np']
        if op==lower_credentials[lower_id]["password"]:
            lower_credentials[lower_id]["password"]=np
            return"""
                    <h1>password change successfully</h1>    """
        else:
            return render_template("change_loo_pass.html")
    else:
        return render_template("change_loo_pass.html")








app.run(debug=True)