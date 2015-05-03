#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template#, g
from flask_bootstrap import Bootstrap

import app


DEBUG = True

SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)


	
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hello')
def hello():
	return render_template('hello.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)