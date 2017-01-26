from app import app, db, models
from flask import render_template

@app.route('/', methods =['POST', 'GET'])
@app.route('/index/', methods =['POST', 'GET'])
def front_page():
    stories = models.Story.newest_posts(page=1)
    return render_template('index.html', entries = stories)