from flask import Flask
from flask_bootstrap import Bootstrap5
import config
import sqlite3

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)

from views.base import *


def db_conn():
    conn = config.DB_CONN
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app.run(port=config.PORT, debug=config.DEBUG)
