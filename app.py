from crypt import methods
import datetime
import imp
import os
from flask import Flask, redirect, render_template, request, make_response, session, url_for, jsonify
from werkzeug.utils import secure_filename
import werkzeug
from flask import json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdbjjasbdbashdas'
UPLOAD_FOLDER = 'media'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    data = ['emp1','emp2','emp3']
    data2 = [{'name': 'Bob', 'job': 'Mgr'},
           {'name': 'Kim', 'job': 'Dev'},
           {'name': 'Sam', 'job': 'Dev'}]
    d = dict(zip(data, data2))
    return jsonify(d)

if __name__ == "__main__":
    app.run()