#!/usr/bin/env python3

from flask import Flask

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

from index import *

if __name__ == '__main__':
    app.run()
