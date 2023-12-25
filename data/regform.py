from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm, SerializerMixin):
    login = StringField("Логин", validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    check = BooleanField('Я согласен(а) с', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')