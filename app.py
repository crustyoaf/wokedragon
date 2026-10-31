import os

from flask import Flask

from commands import seed
from extensions import db, migrate
from routes import bp


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
    else:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(bp)
    app.cli.add_command(seed)

    return app