from models.user import User
from routes.auth import auth
from config import Config
from models import db
from utils.login_manager import login_manager
from flask_login import login_required, current_user
from flask import Flask, redirect, url_for, render_template
from models.problem import Problem
from routes.problems import problems


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth)
app.register_blueprint(problems)


@app.route("/")
def home():
    return redirect(url_for("auth.login"))


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    with app.app_context():
        try:
            db.engine.connect()
            print("✅ Database connected successfully!")
        except Exception as e:
            print("❌ Database connection failed!")
            print(e)

    app.run(debug=True)