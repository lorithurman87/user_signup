from flask import Flask, request, redirect, render_template
import cgi
"""import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
"""
app = Flask(__name__)

app.config['DEBUG'] = True     


@app.route("/", methods=['POST'])

def validate_user():
    username = request.form["username"]
    password = request.form["password"]
    retype_pw = request.form["retype_pw"]
    email = request.form["email"]
    #usernames = request.form["username"]


    if len(username) > 20 or len(username)< 3:
        error = "Please enter a valid username. Usernames must be between 3-20 characters long and cannot include spaces"
        return redirect("/?error=" + error)

    if len(password) > 20 or len(password) < 3:
        error = "Please enter a valid password. Passwords must be between 3-20 characters long and cannot include spaces"
        return (has_an_error(username, email) + error)

    if " " in username:
        error = "Please enter a valid username. Usernames must be between 3-20 characters long and cannot include spaces"
        return redirect("/?error=" + error)

    if " " in password:
        error = "Please enter a valid password. Passwords must be between 3-20 characters long and cannot include spaces"
        return (has_an_error(username, email) + error)
    
    if retype_pw != password:
        error = "Please enter a valid password. Passwords must match"
        username = request.form["username"]
        email = request.form["email"]
        return (has_an_error(username, email) + error)

    if email == "": 
        return verified_user(username)
    if "@" in email and "." in email:
        if len(email) <= 20 and len(email) > 2:
            return verified_user(username)
        else: 
            error = "Please enter a valid email"
            return redirect("/?error=" + error)
    else: 
        error = "Please enter a valid email"
        return redirect("/?error=" + error)
        


@app.route("/error", methods=['POST'])
def has_an_error(username, email):
    return render_template('index.html', username = (username), email = (email))    



@app.route("/welcome", methods=['POST'])
def verified_user(username):
    return  render_template('welcome_page.html', username = username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()