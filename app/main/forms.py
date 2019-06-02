from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class DisplayPost(FlaskForm):
    text = TextAreaField('Type in your pitch', validators=[Required()])
    submit = SubmitField('post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment.', validators=[Required()])
    submit = SubmitField('Submit')
