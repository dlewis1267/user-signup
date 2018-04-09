from flask import Flask, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post" action="/signup">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="">
                        <span class="error">{0}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error">{0}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password">
                        <span class="error">{0}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="">
                        <span class="error">{0}</span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""
"""
@app.route("/signup", methonds=['POST'])

def add_username():
    new_user = request.form['username']

    if len(new_user) > 20:
        error = "{0} do not use more than 20 characters"

    elif len(new_user) < 3:
        error = "{0} do not use less than 3 characters"

    return redirect ("/?error=" + error)

    for char in new_user:
        if char.isspace():
            error = "{0} do not use a space in your username"
        
        return redirect ("/?error=" + error)

def add_password():
    new_password = request.form['password']
    verify_password = request.form['verify']

    if len(new_password) > 20:
        error = "{0} password cannot be greater than 20 characters"

    elif len(new_password) < 3:
        error = "{0} password must be greater than 3 characters"

    elif verify_password != new_password:
        error = "{0} verify password must match password"

    return redirect ("/?error=" + error)

def add_email():
    new_email = request.form['email']
    needed_char = '@.'

    if any char in email != needed_char:
       error = "{0} you must provide a valid email address" 

    return redirect ("/?error=" + error)
"""

@app.route("/")
def index():
    return form.format("")


@app.route("/signup", methods=['POST'])

def add_username():
    new_user = request.form['username']
    error = request.args.get("error")

    if new_user.isspace():
        content ="{0} You must add a user name"

    elif ' ' in new_user:
        content = "{0} do not use a space in your user name"

    elif len(new_user) < 3:
        content = "{0} do not use less than 3 characters"

    elif len(new_user) > 20:
        content = "{0} do not use more than 20 characters"

    else:
        content = "Welcome"
    
    return content
    
def add_password():
    new_password = request.form['password']
    verify_password = request.form['verify']

    if new_password.isspace():
        error = "{0} You must add a password"

    elif len(new_password) > 20:
        error = "{0} password cannot be greater than 20 characters"

    elif len(new_password) < 3:
        error = "{0} password must be greater than 3 characters"

    elif verify_password != new_password:
        error = "{0} verify password must match password"

    else:
        error = "Super"

    return error

def add_email():
    new_email = request.form['email']

    if ' ' in new_email:
        hello = "{0} do not use a space in your email"

    elif len(new_email) < 3:
        hello = "{0} your email cannot be less than 3 characters"

    elif len(new_email) > 20:
        hello = "{0} your email cannot be more than 20 characters"

    elif '@' not in new_email:
        hello = "{0} you must use a @ in your email"

    elif '.' not in new_email:
        hello = "{0} you must use a . in your email"

    else:
        hello = "Welcome"
    
    return hello

app.run()