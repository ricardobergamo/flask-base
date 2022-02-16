#!/usr/bin/venv python

from flask import Flask
import config
import sqlite3

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)


def db_conn():
    conn = config.DB_CONN
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return 'Index'


if __name__ == '__main__':
    app.run(port=config.PORT, debug=config.DEBUG)
