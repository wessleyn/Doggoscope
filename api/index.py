from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, from DoggoScope!'


@app.route('/about')
def about():
    return 'About DoggoScope'
