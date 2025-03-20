from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/submit')
def submit():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
