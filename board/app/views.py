from app import app
from flask import render_template

@app.route('/', methods =['POST', 'GET'])
@app.route('/index/', methods =['POST', 'GET'])
def index():
    return render_template('index.html')