#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing
import json
import gpslib

# configuation
DATABASE = './tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource("schema.sql", mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def init_imgdb():
    with closing(connect_db()) as db:
        with app.open_resource("imgrepo.sql", mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title,text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries(title,text) values(?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/map')
def openmap():
    # flash('open map')
    return render_template('index.html')


@app.route('/gpsdata')
def gpsdata():
    cur = g.db.execute('select igm_x,img_y,img_name from imgrepo')
    basic = [dict(x=row[0], y=row[1], content=row[2]) for row in cur.fetchall()]
    # gps = []
    # for b in basic:
    #     point = {}
    #     point['x'] = b[0]
    #     point['y'] = b[1]
    #     point['content'] = b[2]
    #     gps.append(point)
    return json.dumps(basic, ensure_ascii=True)


@app.route('/init_imgrepo')
def init_imgrepo():
    init_imgdb()
    basic = gpslib.getallimgs()
    gps = []
    for b in basic:
        g.db.execute('insert into imgrepo(img_name,igm_x,img_y) values(?, ?,?)',
                     [b[2], b[0], b[1]])
    g.db.commit()
    return '<h1>OK</h1>'

@app.route('/test')
def test():
    a = ['a','b','c','d','e','f','g','h','i','j','k']
    b = 1
    c = ''
    f = []
    for d in a:
        e = []
        e.append(d)
        e.append(str(b))
        b += 1
        f.append(e)
    entries = [dict(title=row[0], text=row[1]) for row in f]
    return render_template('test.html', entries=entries)


if __name__ == '__main__':
    app.run()