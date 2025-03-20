
from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from modules import User, get_db_connection, bcrypt
from my_secret import SECRET_KEY

from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session # type: ignore


app = Flask(__name__)
app.secret_key = SECRET_KEY  


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

@app.route('/') 
def index():
    return render_template('start.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/submit')
def submit():
    return render_template('home.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']  
        password = request.form['password']
        user = User.get_user_by_email(email)  

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')  # Changed to 'email'
        password = request.form.get('password')
        if User.get_user_by_email(email):  # Changed to 'get_user_by_email'
            flash('Email already taken', 'warning')
        else:
            User.register_user(email, password)  # Changed to 'register_user' with email
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('start'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, debug=True)
