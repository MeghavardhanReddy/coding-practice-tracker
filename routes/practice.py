from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from models import db
from models.problem import Problem
from models.practice import Practice
from forms.practice_form import PracticeForm

practice = Blueprint("practice", __name__)

@practice.route("/practice", methods=["GET", "POST"])
@login_required
def add_practice():

    form = PracticeForm()

    # Load problems of current user
    form.problem.choices = [
        (problem.id, problem.title)
        for problem in Problem.query.filter_by(
            user_id=current_user.user_id
        ).all()
    ]

    if form.validate_on_submit():

        session = Practice(
            user_id=current_user.user_id,
            problem_id=form.problem.data,
            status=form.status.data,
            time_taken=form.time_taken.data,
            attempts=form.attempts.data,
            notes=form.notes.data
        )

        db.session.add(session)
        db.session.commit()

        flash("Practice session saved successfully!", "success")

        return redirect(url_for("practice.add_practice"))

    return render_template(
        "practice.html",
        form=form
    )

@practice.route("/practice-history")
@login_required
def practice_history():

    sessions = Practice.query.filter_by(
        user_id=current_user.user_id
    ).order_by(
        Practice.practice_date.desc()
    ).all()

    return render_template(
        "practice_history.html",
        sessions=sessions
    )