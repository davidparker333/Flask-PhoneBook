from app.models import PhoneNumber
from app.forms import PhoneNumberForm
from app import app, db
from flask import render_template, request, redirect, flash, url_for
#from app.forms import #put your form here

@app.route('/')
def index():
    title = "Phone Numbers 'R Us | Home"
    numbers = PhoneNumber.query.all()

    return render_template('index.html', title=title, numbers=numbers)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "Phone Numbers 'R Us | Register"
    form = PhoneNumberForm()
    if request.method == 'POST':
        name = form.name.data
        phone_number = form.phone_number.data
        existing_user = PhoneNumber.query.filter(PhoneNumber.phone_number == phone_number).all()
        if existing_user:
            flash('That phone number is already in use! Try again', 'danger')
            return redirect(url_for('register'))
        new_phone_number = PhoneNumber(name, phone_number)
        db.session.add(new_phone_number)
        db.session.commit()
        flash(f'Thank you {name}. You have successfully registered!', "success")

        return redirect(url_for('index'))

    return render_template('register.html', title=title, form=form)