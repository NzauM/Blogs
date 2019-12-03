from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required
from ..models import Subscriber

class BlogForm(FlaskForm):
    title = StringField('Enter title ',validators = [Required()])
    blog = TextAreaField('Your Blog',validators = [Required()])
    author = StringField('Your name' , validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment' ,validators= [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateBlog(FlaskForm):
    title = StringField('Enter title',validators=[Required()])
    blog = TextAreaField('Edit your blog',validators = [Required()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    email = StringField("Email Address",validators=[Required()])
    submit = SubmitField("Subscribe")
    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email =data_field.data).first():
            raise ValidationError("Account already subscribed with that email")





