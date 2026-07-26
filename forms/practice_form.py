from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class PracticeForm(FlaskForm):

    problem = SelectField(
        "Problem",
        coerce=int,
        validators=[DataRequired()]
    )

    status = SelectField(
        "Status",
        choices=[
            ("Solved", "Solved"),
            ("Attempted", "Attempted"),
            ("Revision", "Revision")
        ]
    )

    time_taken = IntegerField(
        "Time Taken (minutes)",
        validators=[DataRequired(), NumberRange(min=1)]
    )

    attempts = IntegerField(
        "Attempts",
        validators=[DataRequired(), NumberRange(min=1)]
    )

    notes = TextAreaField("Notes")

    submit = SubmitField("Save Practice Session")