from flask import Flask, redirect, url_for, render_template
from flask_login import login_required, current_user
from config import Config
from models import db
from models.user import User
from sqlalchemy import func

from utils.login_manager import login_manager

from routes.auth import auth
from routes.problems import problems
from routes.practice import practice

from models.problem import Problem
from models.practice import Practice

# Create Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Initialize Login Manager
login_manager.init_app(app)

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Create Tables
with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(problems)
app.register_blueprint(practice)

# Home Route
@app.route("/")
def home():
    return redirect(url_for("auth.login"))

# Dashboard
@app.route("/dashboard")
@login_required
def dashboard():

    total_problems = Problem.query.filter_by(
        user_id=current_user.user_id
    ).count()

    solved = Practice.query.filter_by(
        user_id=current_user.user_id,
        status="Solved"
    ).count()

    attempted = Practice.query.filter_by(
        user_id=current_user.user_id,
        status="Attempted"
    ).count()

    revision = Practice.query.filter_by(
        user_id=current_user.user_id,
        status="Revision"
    ).count()

    total_sessions = Practice.query.filter_by(
        user_id=current_user.user_id
    ).count()

    average_time = db.session.query(
        db.func.avg(Practice.time_taken)
    ).filter_by(
        user_id=current_user.user_id
    ).scalar()

    if average_time is None:
        average_time = 0

    success_rate = 0

    if total_sessions > 0:
        success_rate = round((solved / total_sessions) * 100, 2)

    difficulty_data = db.session.query(
        Problem.difficulty,
        func.count(Problem.id)
    ).filter_by(
        user_id=current_user.user_id
    ).group_by(
        Problem.difficulty
    ).all()

    status_data = db.session.query(
        Practice.status,
        func.count(Practice.id)
    ).filter_by(
        user_id=current_user.user_id
    ).group_by(
        Practice.status
    ).all()

    difficulty_labels = [row[0] for row in difficulty_data]
    difficulty_counts = [row[1] for row in difficulty_data]

    status_labels = [row[0] for row in status_data]
    status_counts = [row[1] for row in status_data]

    return render_template(
    "dashboard.html",
    total_problems=total_problems,
    solved=solved,
    attempted=attempted,
    revision=revision,
    total_sessions=total_sessions,
    average_time=round(average_time, 2),
    success_rate=success_rate,
    difficulty_labels=difficulty_labels,
    difficulty_counts=difficulty_counts,
    status_labels=status_labels,
    status_counts=status_counts
)

# Run Application
if __name__ == "__main__":
    with app.app_context():
        try:
            db.engine.connect()
            print("✅ Database connected successfully!")
        except Exception as e:
            print("❌ Database connection failed!")
            print(e)

    app.run(debug=True)