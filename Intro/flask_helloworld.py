from flask import Flask #import Flask instance from package
app = Flask(__name__)

@app.route('/') #decorator: this will say what website are moving to 
#routes or views which take you to specific page 
def hello_world():
    return '<h1> Hello World! Bigger one, changed <h1>'

"""@app.route('/about')
def about_page():
    return '<h1> This is about page<h1>'"""

#we can also create dynamic routes 
@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is about page is for {username} <h1>'