import os
from flask import *
from sqlite3 import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.random import RandomCard
from data import db_session
from data.donate import buy_pay, im_donate
from data.users import User
from data.loginform import LoginForm
from data.regform import RegisterForm
from data.aiform import Ai
from data.ai_ChatGPT import ai_request
import random
from webbrowser import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'taro_ai'
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
            name=form.name.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        if user and user.check_password(form.password.data):
            login_user(user)
            session['id'] = user.id
            session['login'] = user.login
        try:
            f = request.files['picture']
            split_tup = os.path.splitext(f.filename)
            file_extension = split_tup[1]
            filename = f'{str(user.id)}{file_extension}'
            f.save(os.path.join('static/user_pic', filename))
            user.avatar(user, db_sess, filename)
        except:
            user.picture = 'static/user_pic/unnamed.jpeg'
        return redirect('/Profile')
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
            session['login'] = user.login
            return redirect('/Profile')
        return render_template('log.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('log.html', title='Авторизация', form=form)


@app.route('/menu', methods=['GET', 'POST'])
@login_required
def menu():
    return render_template('Menu.html')


@app.route('/Future', methods=['POST', 'GET'])
@login_required
def Future():
    return render_template('Future.html')


@app.route('/ai', methods=['GET', 'POST'])
@login_required
def ai():
    form = Ai()
    if form.validate_on_submit():
        ai_req = form.ai_req.data
        ai_resp = ai_request(ai_req)
        return render_template('Ai.html', form=form, ai_resp=ai_resp)
    return render_template('Ai.html', form=form, ai_resp="None")


@app.route('/Relation')
@login_required
def Relation():

    return render_template("Relation.html")

@app.route('/Career')
@login_required
def Career():
    return render_template("Career.html")

@app.route('/Money')
@login_required
def Money():
    return render_template("Money.html")

@app.route('/Profile')
@login_required
def user():
    return render_template('Profile.html', login=session['login'])


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

#
# @app.route('/donate')
# @login_required
# def donate():
#     im_donate(session['login'])
#     return redirect("Donate.html")


if __name__ == '__main__':
    db_session.global_init("db/TarAi_Data.db")
    app.run()
