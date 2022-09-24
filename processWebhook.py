import flask
import os

from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='images/favicon.png')
@app.route('/')
@app.route('/home')
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.debug = True
    app.run()