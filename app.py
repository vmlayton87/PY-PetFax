from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "This is the petfax app."

@app.route('/pets/')
def pets():
    return "This is the pets route."