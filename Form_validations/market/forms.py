from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='User Name',validators= [Length(min=2, max=30), DataRequired()] )
    email_address= StringField(label='Email Id', validators= [Email(),DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators= [EqualTo(password1),DataRequired()])
    submit =SubmitField(label='Create Account')