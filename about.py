#!/usr/bin/env python3

from flask import render_template
from hwaware import app
from time import strftime

@app.route('/about')
def on_about():
    year = int(strftime('%Y'))
    past = (year - 2015) * 365
    return render_template('about.html', longness=past)
