from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    register = SubmitField('Register')


class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    sign_in = SubmitField('Sign in', validators=[DataRequired()])

class CreateTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    task = TextAreaField('Task', validators=[DataRequired()])
    create = SubmitField('Create')
