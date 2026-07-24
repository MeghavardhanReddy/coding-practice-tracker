from flask import Blueprint, render_template, redirect, url_for, flash
from forms.auth_forms import RegisterForm
from forms.login_form import LoginForm
from models import db
from models.user import User
from flask_login import login_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        print("Entered Email:", form.email.data)
        print("User Found:", user)

        if user:
            print("Stored Hash:", user.password_hash)
            print("Password Check:", user.check_password(form.password.data))

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

        flash("Registration Successful!", "success")

        return redirect(url_for("auth.register"))

    return render_template("register.html", form=form)