from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class Ai(FlaskForm, SerializerMixin):
    autocomplete_input_theme = StringField('Выберите Тему', validators=[DataRequired()])
    autocomplete_input_card1 = StringField('Выберите карту', validators=[DataRequired()])
    autocomplete_input_card2 = StringField('Выберите карту', validators=[DataRequired()])
    autocomplete_input_card3 = StringField('Выберите карту', validators=[DataRequired()])
    autocomplete_input_card4 = StringField('Выберите карту', validators=[DataRequired()])
    autocomplete_input_card5 = StringField('Выберите карту', validators=[DataRequired()])
    submit = SubmitField('Спросить у Вселенной')