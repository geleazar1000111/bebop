from flask import render_template, flash, redirect, url_for
from app import app
from freebusy.FreeBusyEvent_Builder import FreeBusyEventBuilder
from helpers import auth

# View function: code written to respond to requests to app
# index is our view function
@app.route('/')
@app.route('/index')
def index():
    booked = auth.get_freebusy(auth.get_creds())
    fb = FreeBusyEventBuilder('UR10')
    free = fb.initialize_free_events(booked, 2020, 1, 8, 2020, 1, 9)
    print(free)
    user = {'username': 'UR10'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # rendering converts template to HTML page
    return render_template('index.html', title='Home', user=user, posts=free)

# @app.route('/login')
# def login():
