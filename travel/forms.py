from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Email, EqualTo, length
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG',"JPG", 'JPEG', 'png', 'jpg', 'jpeg', 'jfif'}

class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired(), length(min=4, max=20)])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Destination Image', validators=[
        FileRequired(message= "Image cannot be empty"),
        FileAllowed(ALLOWED_FILE, message= 'Only supports png, jpg, jpeg, JPG, PNG, and JPEG')])
    currency = StringField('Currency', validators=[InputRequired(), length(max=3)])
    submit = SubmitField("Create")

#User login
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = EmailField("Email Address", validators=[Email("Please enter a valid email"), length(min=4, max=20)])
    
    #linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match"), length(min=8, max=20)])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")
    
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')