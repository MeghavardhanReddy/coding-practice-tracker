from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Optional


class ProblemForm(FlaskForm):

    title = StringField(
        "Problem Title",
        validators=[DataRequired()]
    )

    platform = SelectField(
        "Platform",
        choices=[
            ("LeetCode", "LeetCode"),
            ("CodeChef", "CodeChef"),
            ("Codeforces", "Codeforces"),
            ("HackerRank", "HackerRank"),
            ("GeeksforGeeks", "GeeksforGeeks")
        ]
    )

    difficulty = SelectField(
        "Difficulty",
        choices=[
            ("Easy", "Easy"),
            ("Medium", "Medium"),
            ("Hard", "Hard")
        ]
    )

    topic = StringField(
        "Topic",
        validators=[DataRequired()]
    )

    problem_link = StringField(
        "Problem Link",
        validators=[Optional(), URL()]
    )

    notes = TextAreaField("Notes")

    submit = SubmitField("Add Problem")