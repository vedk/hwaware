#!/usr/bin/env python3

from hwaware import app
from flask import render_template, request
from time import strftime

classes = {'10F': '10th Faith',
           '10C': '10th Courage',
           '10H': '10th Hope',
           '9F' : '9th Faith',
           '9H' : '9th Hope',
           '8F' : '8th Faith',
           '8H' : '8th Hope'}

@app.route('/', methods=['GET', 'POST'])
def on_index():
    y = int(strftime('%Y'))
    if y == 2016:
        footer = '&copy; ' + str(y) + ' Ved Khandekar'
    else:
        footer = '&copy; 2016 - ' + str(y) + ' Ved Khandekar'

    if request.method == 'POST':
        try:
            usrclass = request.form['usrclass']
            since = int(request.form['nsince'])
            print(usrclass)
        except ValueError:
            since = 3 # show the homework of the last three days by default

        # todo: get the data from DB and send it to render_template

    return render_template('index.html', footertext=footer, classes_data=classes)
