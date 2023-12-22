from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class Pic(FlaskForm, SerializerMixin):
    submit = SubmitField('Изменить')