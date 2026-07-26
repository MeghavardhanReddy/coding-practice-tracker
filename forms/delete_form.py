from flask_wtf import FlaskForm
from wtforms import HiddenField


class DeleteForm(FlaskForm):
    """Minimal form used solely to generate a CSRF token for POST-only delete actions."""
    pass
