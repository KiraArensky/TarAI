import os
import sqlite3
from flask import *
from sqlite3 import *
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session
from data.users import User
from data.loginform import LoginForm
from data.regform import RegisterForm
from data.aiform import Ai
from data.ai_ChatGPT import ai_request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'taro_ai'
#
#
# con = sqlite3.connect('TarAi_Data.db', check_same_thread=False)
# cursor = con.cursor()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
#                 id INTEGER,
#                 login TEXT,
#                 password TEXT
#                 )""")
# con.commit()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def main():
    return redirect("/login")


@app.route('/registr', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('Reg.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == form.login.data).first():
            return render_template('Reg.html', title='Регистрация',
                                   form=form,
                                   message="Такой логин занят")
        user = User(
            login=form.login.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('Reg.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def log():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            session['id'] = user.id
            return redirect("/menu")
        return render_template('log.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('log.html', title='Авторизация', form=form)


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('Menu.html')

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    form = Ai()
    if form.validate_on_submit():
        ai_req = form.ai_req.data
        ai_resp = ai_request(ai_req)
        return render_template('Ai.html', form=form, ai_resp=ai_resp)
    return render_template('Ai.html', form=form, ai_resp="None")

# @app.route('/<login>')
# def user(login):
#     db_sess = db_session.create_session()
#     user = db_sess.query(User).filter(User.login == login).first()
#     if user == None:
#         flash('User ' + login + ' not found.')
#         return redirect('/login')
#     return render_template('user.html', ser=user)
#
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/TarAi_Data.db")
    app.run()
