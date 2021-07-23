from sys import modules
from flask import Flask, render_template, request, session, url_for, redirect, g
import model

app = Flask(__name__)

app.secret_key = "jumpingjacz"

username = ''

# List of Users in the database
user = model.check_users()

@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        g.user = session['username']
        return render_template("football.html", message="You are logged in!")
    return render_template("homepage.html", message="Log in to the page or Sign Up!")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # If a previous user was still logged in, process the login, redirect to homepage.html
        session.pop(username, None)
        areYouTheUser = request.form['username']
        passwordForTheUser = model.check_password(areYouTheUser)
        if request.form['password'] == passwordForTheUser:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

    return render_template("index.html")


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'GET':
#         return render_template('index.html')
#     else:
#         username = request.form["username"]
#         password = request.form["password"]
#         db_password = model.check_password(username)

#         if password == db_password:
#             message = model.show_color(username)
#             return render_template("football.html", username=username, message=message)
#         else:
#             error_message = "Password and Username did not checkout."
#             return render_template("index.html", message = error_message)


# This defines what happens before the request
@app.before_first_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


# Get the username in the session
@app.route('/getsession')
def getsession():
    if 'username' in  session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop(username, None)
    return redirect(url_for('login'))

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = "Please sign up."
        return render_template('signup.html', message=message)
    else:
        username = request.form["username"]
        password = request.form["password"]
        favorite_color = request.form["favorite_color"]
        message = model.signup(username, password, favorite_color)
        return render_template('signup.html', message=message)


if __name__  == '__main__':
    app.run(debug=True)