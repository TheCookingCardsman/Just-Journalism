from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/index.html')
def index():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            username = 'admin'
            session['logged_in'] = True
            return home()
        else:
            flash('wrong password!')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
