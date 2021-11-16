from market import app
from flask import render_template
from market.models import Item

@app.route('/') #decorator: this will say what website are moving to 
#routes or views which take you to specific page 
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items)