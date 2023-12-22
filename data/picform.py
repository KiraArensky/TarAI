from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Pic(FlaskForm, SerializerMixin):
    images = ['jpg', 'jpeg', 'jpe', 'jfif',
              'png',
              'gif',
              'tiff', 'tif',
              'bmp',
              'ico',
              'webp',
              'ppm',
              'pgm',
              'jp2']
    new_avatar = FileField('New Avatar', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    submit = SubmitField('Изменить')
