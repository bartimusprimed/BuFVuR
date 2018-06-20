from flask import Flask, render_template, url_for
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    # We are just returning the index.html
    return render_template('index.html')
