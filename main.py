from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('hello_form.html')


@app.route("/signup", methods=['POST'])

def add_newuser():
    new_username = request.form['username']
    new_password = request.form['password']
    verify_password = request.form['verify']
    new_email = request.form['email']
    error = request.args.get("error")

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if ' ' in new_username:
        username_error = "Do not use a space in your name"

    elif len(new_username) < 1:
        username_error = "You must add a user name"

    elif len(new_username) < 3:
        username_error = "Do not use less than 3 characters in your name"

    elif len(new_username) > 20:
        username_error = "Do not use more than 20 characters"

    if len(new_password) < 1:
        password_error = "You must add a password"

    elif len(new_password) < 3:
        password_error = "Password must be greater than 3 characters"
    
    elif len(new_password) > 20:
        password_error = "Password cannot be greater than 20 characters"

    if len(verify_password) < 1:
        verify_error = "You must verify your password"

    elif verify_password != new_password:
        verify_error = "Verify password must match password"

    if ' ' in new_email:
        email_error = "Do not use a space in your email"

    elif len(new_email) < 1:
        email_error = email_error

    elif len(new_email) < 3:
        email_error = "Your email cannot be less than 3 characters"

    elif len(new_email) > 20:
        email_error = "Your email cannot be more than 20 characters"

    elif '@' not in new_email:
        email_error = "You must use a @ in your email"

    elif '.' not in new_email:
        email_error = "You must use a . in your email"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('greeting.html',
        new_username = new_username
        )

    return render_template('hello_form.html', 
    username_error = username_error, 
    password_error = password_error,
    verify_error = verify_error,
    email_error = email_error
    )


app.run()