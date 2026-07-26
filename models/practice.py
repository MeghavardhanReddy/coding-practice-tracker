from models import db
from datetime import datetime

class Practice(db.Model):
    __tablename__ = "practice"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    problem_id = db.Column(
        db.Integer,
        db.ForeignKey("problems.id"),
        nullable=False
    )

    status = db.Column(db.String(20), nullable=False)
    time_taken = db.Column(db.Integer)
    attempts = db.Column(db.Integer)
    notes = db.Column(db.Text)

    practice_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # ✅ Add this relationship
    problem = db.relationship("Problem", backref="practice_sessions")