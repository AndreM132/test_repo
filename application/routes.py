from flask import request
from application import app


@app.route('/home')
@app.route('/')
def home():
    
    return "Hello World"
