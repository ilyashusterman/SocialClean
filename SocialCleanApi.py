# from logging import DEBUG
from flask import Flask, render_template, request, flash, redirect, url_for
import tensorflow as tf

app = Flask(__name__)
# app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\x87\x98g\xc3\xbd\xd8r\x99\xb9\x85p\xc1\xca8p\x94\xe5\xf0\x82\x89\xb6p,\xe1'

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}".format(self.firstname[0], self.lastname[0])


@app.route('/test')
def test():
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    return 'Thermos test working GET! {}'.format(sess.run(hello))


@app.route('/')
@app.route('/index')
def index():
    return "hello"


@app.route('/add', methods=['GET', 'POST'])
def add():
    return "get response"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)  # to get app running in debug is debug=True

