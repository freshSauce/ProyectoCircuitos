from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    from ..models import User

    db.init_app(app)
    with app.app_context():
        db.create_all()
