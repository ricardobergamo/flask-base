import os
import sqlite3

# Sistema
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = '5000'
SECRET_KEY = '\x87*\xfb\xfd!\xa5\x9bz\x14\xc4\xaf'
ENV_DIR = BASE_DIR + '/venv/py3'
STATIC_DIR = BASE_DIR + '/static'

# Aplicativo
NAME = 'Base'
AUTOR = 'Autor'
TITLE = 'Flask APP'
VERSAO = '0.1'
APP_DIR = '/var/www/htdocs/' + NAME

# Sqlite Database
DB_NAME = 'app.db'
DB_DIR = BASE_DIR + '/database/'
DB_CONN = sqlite3.connect(DB_DIR + DB_NAME)
