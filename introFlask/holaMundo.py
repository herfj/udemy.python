from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola Mundo'
#METHODS GET, POST, PUT, DELETE, PATCH
@app.route('/post/<post_id>', methods=['POST', 'GET'])
def post(post_id):
    return 'el id de post: ' + post_id

@app.route('/lele', methods=['POST', 'GET'])
def lele():
    # return '  ----  ' +url_for('post', post_id=2)
    # abort(401)
    # return redirect(url_for('post', post_id=2))
    return render_template('lele.html')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='hola Mundo')