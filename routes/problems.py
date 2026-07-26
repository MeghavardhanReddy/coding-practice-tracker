from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from models import db
from models.problem import Problem
from forms.problem_form import ProblemForm

problems = Blueprint("problems", __name__)


@problems.route("/add-problem", methods=["GET", "POST"])
@login_required
def add_problem():

    form = ProblemForm()

    if form.validate_on_submit():

        problem = Problem(
            user_id=current_user.user_id,
            title=form.title.data,
            platform=form.platform.data,
            difficulty=form.difficulty.data,
            topic=form.topic.data,
            problem_link=form.problem_link.data,
            notes=form.notes.data
        )

        db.session.add(problem)
        db.session.commit()

        flash("Problem added successfully!", "success")

        return redirect(url_for("dashboard"))

    return render_template("add_problem.html", form=form)

@problems.route("/problems")
@login_required
def view_problems():

    problems_list = Problem.query.filter_by(
        user_id=current_user.user_id
    ).all()

    return render_template(
        "view_problems.html",
        problems=problems_list
    )


@problems.route("/edit-problem/<int:id>", methods=["GET", "POST"])
@login_required
def edit_problem(id):

    problem = Problem.query.filter_by(
        id=id,
        user_id=current_user.user_id
    ).first_or_404()

    form = ProblemForm(obj=problem)

    if form.validate_on_submit():

        problem.title = form.title.data
        problem.platform = form.platform.data
        problem.difficulty = form.difficulty.data
        problem.topic = form.topic.data
        problem.problem_link = form.problem_link.data
        problem.notes = form.notes.data

        db.session.commit()

        flash("Problem updated successfully!", "success")

        return redirect(url_for("problems.view_problems"))

    return render_template(
        "edit_problem.html",
        form=form
    )

@problems.route("/delete-problem/<int:id>", methods=["POST"])
@login_required
def delete_problem(id):

    problem = Problem.query.filter_by(
        id=id,
        user_id=current_user.user_id
    ).first_or_404()

    db.session.delete(problem)
    db.session.commit()

    flash("Problem deleted successfully!", "success")

    return redirect(url_for("problems.view_problems"))