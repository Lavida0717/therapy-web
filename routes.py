from flask import render_template, redirect, url_for, flash
from . import db
from .models import Booking
from .forms import BookingForm

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking(name=form.name.data, email=form.email.data, date=form.date.data)
        db.session.add(booking)
        db.session.commit()
        flash('Your booking has been made!', 'success')
        return redirect(url_for('confirm'))
    return render_template('book.html', form=form)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')
