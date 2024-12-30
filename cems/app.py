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
    pass

@app.route('/regloo',methods=['GET', 'POST'])
def regloo():
    pass

@app.route('/remhio',methods=['GET', 'POST'])
def remhio():
    pass

@app.route('/remloo',methods=['GET', 'POST'])
def remloo():
    pass

@app.route('/hio_changepasss',methods=['GET', 'POST'])
def hio_changepasss():
    pass