from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,NumberRange
from app.models import User

class LoginForm(FlaskForm):
    userId = IntegerField('ID',validators=[NumberRange(min=10000,max=30000,message='Out Of Range')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    userId = IntegerField('ID',validators=[NumberRange(min=10000,max=30000,message='Out Of Range')])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')