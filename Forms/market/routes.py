from werkzeug import datastructures
from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User, db
from market.forms import RegisterForm

@app.route('/') #decorator: this will say what website are moving to 
#routes or views which take you to specific page 
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/register', methods=['POST','GET'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username= form.username.data,
                              email_address= form.email_address.data,
                              password_hash =form.password1.data,
                                ) 
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    return render_template('register.html',form= form)

