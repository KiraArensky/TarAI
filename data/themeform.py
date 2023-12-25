from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class ThemeF(FlaskForm, SerializerMixin):
    input_theme = StringField(validators=[DataRequired()])
    submit = SubmitField('Спросить у Вселенной')