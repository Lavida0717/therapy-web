from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BookingForm
from __init__ import create_app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app = create_app()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    from models import Booking  # Import here to avoid circular import
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

if __name__ == '__main__':
    app.run(debug=True)
