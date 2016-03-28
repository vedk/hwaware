#!/usr/bin/env python3

from flask import render_template
from hwaware import app
from datetime import datetime

@app.route('/about')
def on_about():
    then = datetime(2015, 6, 15, 7, 15)
    secondspast = (datetime.now() - then).total_seconds()
    
    return render_template('about.html', longness=secondspast)
