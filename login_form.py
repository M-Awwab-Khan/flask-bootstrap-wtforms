from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(8, 12)])
    submit = SubmitField(label='Go')
