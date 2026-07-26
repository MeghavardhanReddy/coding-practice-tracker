from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from models import db
from models.problem import Problem
from models.practice import Practice
from forms.practice_form import PracticeForm
from forms.delete_form import DeleteForm

practice = Blueprint("practice", __name__)

# Status ranking for the "only upgrade" rule
STATUS_RANK = {
    "Not Started": 0,
    "Attempted": 1,
    "Revision": 2,
    "Solved": 3
}


def _sync_problem_status(problem, new_session_status):
    """Upgrade Problem.status if the new practice session status is higher ranked."""
    current_rank = STATUS_RANK.get(problem.status, 0)
    new_rank = STATUS_RANK.get(new_session_status, 0)
    if new_rank > current_rank:
        problem.status = new_session_status


@practice.route("/practice", methods=["GET", "POST"])
@login_required
def add_practice():

    form = PracticeForm()

    # Load problems belonging to the current user
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

        # Sync Problem.status (only upgrade, never downgrade)
        problem = Problem.query.get(form.problem.data)
        if problem:
            _sync_problem_status(problem, form.status.data)

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

    delete_form = DeleteForm()

    return render_template(
        "practice_history.html",
        sessions=sessions,
        delete_form=delete_form
    )


@practice.route("/edit-practice/<int:id>", methods=["GET", "POST"])
@login_required
def edit_practice(id):

    session = Practice.query.filter_by(
        id=id,
        user_id=current_user.user_id
    ).first_or_404()

    form = PracticeForm(obj=session)

    # Load problems for the dropdown
    form.problem.choices = [
        (problem.id, problem.title)
        for problem in Problem.query.filter_by(
            user_id=current_user.user_id
        ).all()
    ]

    if form.validate_on_submit():

        session.problem_id = form.problem.data
        session.status = form.status.data
        session.time_taken = form.time_taken.data
        session.attempts = form.attempts.data
        session.notes = form.notes.data

        # Re-sync Problem.status after edit
        problem = Problem.query.get(form.problem.data)
        if problem:
            _sync_problem_status(problem, form.status.data)

        db.session.commit()

        flash("Practice session updated successfully!", "success")

        return redirect(url_for("practice.practice_history"))

    return render_template(
        "edit_practice.html",
        form=form,
        session=session
    )


@practice.route("/delete-practice/<int:id>", methods=["POST"])
@login_required
def delete_practice(id):

    session = Practice.query.filter_by(
        id=id,
        user_id=current_user.user_id
    ).first_or_404()

    db.session.delete(session)
    db.session.commit()

    flash("Practice session deleted successfully!", "success")

    return redirect(url_for("practice.practice_history"))