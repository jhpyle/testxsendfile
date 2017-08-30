import time
from flask import Flask, render_template
app = Flask(__name__)

app.config['USE_X_SENDFILE'] = True

@app.route('/')
def index():
    return render_template('test.html')

@app.before_request
def before_request():
    time.sleep(0.25)
