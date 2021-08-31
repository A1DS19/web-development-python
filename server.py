from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<username>')
def hello(username=None):
    return render_template('index.html', username=username)
