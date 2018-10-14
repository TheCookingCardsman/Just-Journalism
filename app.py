from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

tempName = "Not working"

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
        result = query.first()
        if result:
            session['logged_in'] = True
            return render_template('index.html')
        else:
            flash('wrong password!')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if request.form['confirmpassword'] == request.form['password'] and request.form['username'] != '' and request.form['e-mail'] != '' and request.form['password'] != '':
            session['logged_in'] = True
            tempName = request.form['username']
            #print(tempName)
            #return render_template('index.html')
            print(tempName)
            return render_template('index.html', tempName = tempName)
    return render_template('signup.html')


@app.route('/index.html')
def index():
    if not session.get('logged_in'):
        print("not logged")
        return render_template('index.html')
    else:
        print("logged")
        #request.form['User'] = tempName
        return render_template('index.html')

@app.route('/political.html')
def politics():
    if not session.get('logged_in'):
        return render_template('loggedout.html')
    else:
        return render_template('political.html')

@app.route('/sports.html')
def sports():
    if not session.get('logged_in'):
        return render_template('loggedout.html')
    else:
        return render_template('sports.html')

@app.route('/health.html')
def health():
    if not session.get('logged_in'):
        return render_template('loggedout.html')
    else:
        return render_template('health.html')

@app.route('/loggedout.html')
def loggedout():
    return render_template('loggedout.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         if request.form['password'] == 'password' and request.form['username'] == 'admin':
#             username = 'admin'
#             session['logged_in'] = True
#             return home()
#         else:
#             flash('wrong password!')
#     return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
