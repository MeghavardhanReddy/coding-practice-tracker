from models import db
from datetime import datetime, timezone


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
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Practice problem_id={self.problem_id} status={self.status}>"