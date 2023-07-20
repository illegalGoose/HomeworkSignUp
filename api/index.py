from flask import Flask, request, Response, redirect, url_for
from helpfulFunctions import valid_username, valid_password, valid_email, passwords_match
import os
import jinja2
app = Flask(__name__)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


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
            return t.render(invalid_username="Username is invalid!")
        if not password:
            return t.render(invalid_password="Password is invalid!")
        if not verify_password:
            return t.render(passwords_missmatch="Passwords didn't match!", value=user_name)
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