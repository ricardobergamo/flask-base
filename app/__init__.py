import os
from flask import Flask
from flask_bootstrap import Bootstrap5


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    bootstrap = Bootstrap5(app)

    app.config.from_object('app.config')
    app.config.from_pyfile(os.path.join(app.instance_path, 'config.py'), silent=True)


    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from .views import base
    app.register_blueprint(base.bp)

    return app
