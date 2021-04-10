from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    desc=TextAreaField('Description',validators=[DataRequired()])   
    photo= FileField('Photo',validators=[FileRequired(), FileAllowed(['jpg','png'])])