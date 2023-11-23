from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    user_input = StringField(label="", validators=[DataRequired()], render_kw={"autofocus": True})
    submit = SubmitField(label="Submit")
