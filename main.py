from flask import Flask, request, redirect,render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/validate_user", methods=['POST'])
def validate_user():

    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    user_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''

    f_username = len(username)-username.count(' ')

    errors = [] 
    if request.method == 'post':     
        return render_template('welcome.html', errors=errors)

    if username == '' :
       user_error = "That's not a valid username"      
       return render_template('index.html',user_error=user_error)

    if len(username) < 3:
       user_error = "That's not a valid username"     
       return render_template('index.html',user_error=user_error)  

    if len(username) > 20:
       user_error = "That's not a valid username"      
       return render_template('index.html',user_error=user_error) 
    
    if f_username < 3:
       user_error = "That's not a valid username"      
       return render_template('index.html',user_error=user_error)

    if password == '':
       password_error = "That' s not a valid password"
       return render_template('index.html',password_error=password_error)

    if len(password) < 3:
        password_error = "That' s not a valid password"
        return render_template('index.html',password_error = password_error )

    if len(password) > 20:
        password_error = "That 's not a valid password"
        return render_template('index.html',password_error = password_error )

    if password != vpassword:
       vpassword_error = "Passwords don't match"
       return render_template('index.html',vpassword_error = vpassword_error )

    if email =='':
        return render_template('welcome.html',title='welcome',username=username)

    if (len(email)<3) and (len(email)<20) and re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',email):
        email_error = "That 's not a valid email"
        return render_template('index.html',email_error = email_error )

    if (len(email)>3) and (len(email)<20) and re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',email):
        return render_template('welcome.html',title='welcome',username=username)        
    else:
         return render_template('index.html')    

@app.route('/')
def index():
    error = request.args.get('error')
    username = request.args.get('username')
    #use jinja2 templates to create HTML response
    return render_template('index.html')
 

app.run() 
