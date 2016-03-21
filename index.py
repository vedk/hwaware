#!/usr/bin/env python3

from hwaware import app
from flask import render_template
from time import strftime

classes = {'10F': '10th Faith',
           '10C': '10th Courage',
           '10H': '10th Hope',
           '9F' : '9th Faith',
           '9H' : '9th Hope'}

@app.route('/')
def on_index():
    y = int(strftime('%Y'))
    if y == 2016:
        footer = '&copy; ' + str(y) + ' Ved Khandekar'
    else:
        footer = '&copy; 2016 - ' + str(y) + ' Ved Khandekar'

    return render_template('index.html', footertext=footer, classes_data=classes)
