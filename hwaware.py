#!/usr/bin/env python3

from flask import Flask

DEBUG = True
DATABASE = '/home/ved/Documents/'
USERNAME = 'root'
PASSWORD = 'root'

app = Flask(__name__)
app.config.from_object(__name__)

from index import *

if __name__ == '__main__':
    app.run()
