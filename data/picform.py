from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired

class Pic(FlaskForm, SerializerMixin):
    new_avatar = FileField('New Avatar', validators=[FileRequired()])
    submit = SubmitField('Изменить')