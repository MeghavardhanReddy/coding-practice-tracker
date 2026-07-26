from models import db

class Problem(db.Model):
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    title = db.Column(db.String(200), nullable=False)

    platform = db.Column(db.String(50), nullable=False)

    difficulty = db.Column(db.String(20), nullable=False)

    topic = db.Column(db.String(100), nullable=False)

    problem_link = db.Column(db.String(300))

    notes = db.Column(db.Text)

    status = db.Column(
        db.String(20),
        default="Not Started"
    )

practice_sessions = db.relationship(
    "Practice",
    backref="problem",
    lazy=True,
    cascade="all, delete-orphan"
)