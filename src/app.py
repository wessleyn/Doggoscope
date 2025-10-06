import os
import time

from flask import Flask, render_template, request

template_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['dog-image']
        if file:
            file.save(os.path.join(app.static_folder, 'uploads', file.filename))
            # time.sleep(100)  # Delay execution for about 100 seconds, equiv to time spent analysing image
            return render_template('index.html', filename=file.filename)

    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
