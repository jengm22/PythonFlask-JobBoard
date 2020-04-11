import flask
from flask import render_template
app = flask.Flask(__name__)

@app.route('/')
def jobs():
 return render_template('index.html')

@app.route('/')
def index1():
    pass

@app.route('/jobs')
def index2():
    pass