from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class Ai(FlaskForm, SerializerMixin):
    ai_req = StringField('Вопрос', validators=[DataRequired()])
    submit = SubmitField('Отправить')