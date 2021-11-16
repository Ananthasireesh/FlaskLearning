from flask import Flask,render_template

app = Flask(__name__)

@app.route('/') #decorator: this will say what website are moving to 
#routes or views which take you to specific page 
@app.route('/home')
def home_page():
    return render_template('home.html')