from app import app

@app.route('/', methods =['POST', 'GET'])
@app.route('/index/', methods =['POST', 'GET'])
def index():
    return 'hello world'