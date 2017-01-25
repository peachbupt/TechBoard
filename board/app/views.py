from app import app, db, models
from flask import render_template

@app.route('/', methods =['POST', 'GET'])
@app.route('/index/', methods =['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/newest', defaults={'page': 1})
@app.route('/newest/', defaults={'page': 1})
@app.route('/newest/page_<page>')
def newest(page):
    stories = models.Story.newest_posts(page=page)
    print stories
    start = (page - 1) * 20 + 1
    return render_template('newest.html', stories=stories, start=start)