from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    bedroom_number = StringField('Number of Bedrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
