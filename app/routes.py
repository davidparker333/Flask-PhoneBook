import re
from app.models import User
from app.forms import LoginForm, RegisterForm
from app import app, db, mail
from flask_mail import Message
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from flask import render_template, request, redirect, flash, url_for
#from app.forms import #put your form here

@app.route('/')
def index():
    title = "Phone Numbers 'R Us | Home"
    user = User.query.all()

    return render_template('index.html', title=title, user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "Phone Numbers 'R Us | Register"
    form = RegisterForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash("Something in your entry wasn't quite right. Please try again. Make sure your phone number is in XXX-XXX-XXXX format!", 'danger')
            return redirect(url_for('register'))
        name = form.name.data
        username = form.username.data
        phone_number = form.phone_number.data
        email = form.email.data
        password = form.password.data
        existing_user = User.query.filter((User.phone_number == phone_number) | (User.username == username) | (User.email == email)).all()
        if existing_user:
            flash('That phone number is already in use! Try again', 'danger')
            return redirect(url_for('register'))
        new_user = User(name, username, phone_number, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Thank you {name}. You have successfully registered!', "success")

        msg = Message("You signed up for Phone Numbers 'R Us!", recipients=[email])
        msg.body = f"Thank you {name} for signing up to be doxxed by Phone Numbers 'R Us. We'll be sharing your information with strangers in no time. Please enjoy the strange phone calls and emails you will receive in the coming days."
        mail.send(msg)

        return redirect(url_for('index'))

    return render_template('register.html', title=title, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Phone Numbers 'R Us | Login"
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Incorrect username or password. Please try again', 'danger')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        flash("You've successfully logged in. Good job", 'success')
        return redirect(url_for('index'))

    return render_template('login.html', form=form, title=title)

@app.route('/logout')
def logout():
    logout_user();
    flash("You've been logged out", 'warning')
    return redirect(url_for('index'))