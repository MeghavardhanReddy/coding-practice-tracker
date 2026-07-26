from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from forms.auth_forms import RegisterForm
from forms.login_form import LoginForm
from models import db
from models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login Successful!", "success")
            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("Email already exists!", "danger")
            return render_template("register.html", form=form)

        user = User(
            full_name=form.full_name.data,
            email=form.email.data
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful! Please log in.", "success")

        # Fixed: redirect to login after successful registration
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "success")
    return redirect(url_for("auth.login"))