from flask import Flask, render_template, url_for
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    url_for('static', filename='bulma.css')
    url_for('static', filename='vue.js')
    return render_template('index.html')
