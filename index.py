#!/usr/bin/env python3

from hwaware import app
from flask import render_template
from time import strftime

@app.route('/')
def on_index():
    y = int(strftime('%Y'))
    if y == 2016:
        footer = '&copy; ' + str(y) + ' Ved Khandekar'
    else:
        footer = '&copy; 2016 - ' + str(y) + ' Ved Khandekar'

    return render_template('index.html', footertext=footer)
