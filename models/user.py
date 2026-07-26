from flask_login import UserMixin
from models import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    joined_date = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )

    # Relationships — must be inside the class body
    problems = db.relationship(
        "Problem",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    practice_sessions = db.relationship(
        "Practice",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return f"<User {self.full_name}>"