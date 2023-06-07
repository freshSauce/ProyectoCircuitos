from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from ..database import db

bcrypt = Bcrypt()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(512))

    @staticmethod
    def get(username):
        return User.query.filter_by(username=username).first()

    def get_id(self):
        return self.username

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def create_user(username, password):
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user
