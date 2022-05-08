import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('blog.html')

app.run(debug=True)