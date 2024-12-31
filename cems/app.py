from flask import Flask, request,render_template,redirect,url_for,jsonify,flash

app = Flask(__name__)


higher_credentials={"100":{"password":"police@123"},
                    "101":{"password":"swaroop@123"}}
lower_credentials={"10":{"password":"tiru@123"},
                   "11":{"password":"ashok@123"}}



@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('login.html')

@app.route('/higher_login',methods=['GET', 'POST'])
def higher_login():
    global higher_credentials
    id=request.form['id']
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
    password=request.form['password']
    if (id in lower_credentials) and (password == lower_credentials[id]["password"]):
        print(lower_credentials[id])
        return render_template('lower_home.html')
    else:
        return render_template("login.html",msg="invalid credentials")



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
    pass