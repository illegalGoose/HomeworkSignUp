from flask import Flask, request, Response, redirect, url_for
import re
import os
import jinja2
app = Flask(__name__)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

USER_NAME = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
USER_PASSWORD = re.compile(r"^.{3,20}$")
USER_EMAIL = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


def valid_username(username):
    return USER_NAME.match(username)

def valid_password(password):
    return USER_PASSWORD.match(password)

def passwords_match(password, verify_password):
    if password == verify_password:
        return password
    else:
        return None

def valid_email(email):
    if email != '':
        return USER_EMAIL.match(email)
    return True

@app.route("/signup", methods=['GET', 'POST'])
def form():
    t = jinja_env.get_template("signUp.html")
    if request.method == 'POST':
        user_name = request.form["username"] 
        user_password = request.form["password"]
        user_verify_password = request.form["verify"]
        user_email = request.form["email"]

        username = valid_username(user_name)
        password = valid_password(user_password)
        verify_password = passwords_match(user_password, user_verify_password)
        email = valid_email(user_email)
        if not username:
            if not password:
                return t.render(invalid_password="Password is invalid!", invalid_username="Username is invalid!", value=user_name)
            if not verify_password:
                return t.render(passwords_missmatch="Passwords didn't match!", invalid_username="Username is invalid!", value=user_name)
            return t.render(invalid_username="Username is invalid!", value=user_name)
        if not password:
            return t.render(invalid_password="Password is invalid!", value=user_name)
        if not verify_password:
            return t.render(passwords_missmatch="Passwords didn't match!", value=user_name)
        if not email:
            return r.render(invalid_email="Email is invalid!" value= user_name)
        else:
            return redirect("/welcome?username=" + user_name)
    return t.render()

@app.route("/welcome")
def welcome_page():
    t = jinja_env.get_template("welcome.html")
    username = request.args.get("username")
    return t.render(username=username)


if __name__ == "__main__":
    app.run()