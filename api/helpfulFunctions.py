import re

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

