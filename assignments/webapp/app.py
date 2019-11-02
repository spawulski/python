"""
My first Python web app.

Use flask to build a basic web application.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render index.html."""
    return render_template('index.html')


@app.route('/cakes')
def cakes():
    """Render cakes.html."""
    return render_template('cakes.html')


@app.route('/hello/<name>')
def hello(name):
    """Render page.html and take in an argument."""
    return render_template('page.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
