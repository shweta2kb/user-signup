from flask import Flask, request, redirect,render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def validate_user():

    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''
    
    if request.method == 'post':     
        return render_template('welcome.html', errors=errors)
        

    if username == "" or " " in username or len(username) < 3 or len(username) > 20:  
       username_error = "That's not a valid username"      

    if password == "" or " " in password or len(password) < 3 or len(password) > 20:
       password_error = "That' s not a valid password"

    if vpassword != password:
       vpassword_error = "Passwords don't match"

    if email != "":    

        if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
                email_error = "That 's not a valid email"  

    if email_error == "" and username_error == "" and vpassword_error == "" and password_error == "":
            return render_template("welcome.html", username = username) 
    else:
        return render_template("index.html", username_error = username_error, 
                                            password_error = password_error, 
                                            vpassword_error = vpassword_error, 
                                            email_error = email_error, 
                                            username = username, 
                                            email = email) 

@app.route('/')
def index():
    error = request.args.get('error')
    username = request.args.get('username')
    #use jinja2 templates to create HTML response
    return render_template('index.html')
 

app.run() 
