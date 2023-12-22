import os
from flask import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data.picform import Pic
from data.random import RandomCard, save_tarot_user, Slovar

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


@app.errorhandler(401)
def not_found(error):
    return redirect("/login")


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
            session['name'] = user.name
            user.avatar(user, db_sess, 'unnamed.jpg')
            session['picture'] = user.picture
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
    Freddy = RandomCard()
    a = Freddy[0]
    b = Freddy[1]
    c = Freddy[2]

    Freddy_Old = RandomCard()
    d = Freddy_Old[0]
    e = Freddy_Old[1]
    f = Freddy_Old[2]

    save_tarot_user(session['id'], a, b, c, d, e, f, 'love')

    return render_template("Relation.html", First_Card=a, Second_Card=b, Third_Card=c,
                           First_Card_Old=d, Second_Card_Old=e, Third_Card_Old=f, Slovar=Slovar)


@app.route('/Career')
@login_required
def Career():
    Freddy = RandomCard()
    a = Freddy[0]
    b = Freddy[1]
    c = Freddy[2]

    Freddy_Old = RandomCard()
    d = Freddy_Old[0]
    e = Freddy_Old[1]
    f = Freddy_Old[2]

    return render_template("Career.html", First_Card=a, Second_Card=b, Third_Card=c,
                           First_Card_Old=d, Second_Card_Old=e, Third_Card_Old=f, Slovar=Slovar)


@app.route('/Health')
@login_required
def Health():
    Freddy = RandomCard()
    a = Freddy[0]
    b = Freddy[1]
    c = Freddy[2]

    Freddy_Old = RandomCard()
    d = Freddy_Old[0]
    e = Freddy_Old[1]
    f = Freddy_Old[2]

    return render_template("Health.html", First_Card=a, Second_Card=b, Third_Card=c,
                           First_Card_Old=d, Second_Card_Old=e, Third_Card_Old=f, Slovar=Slovar)


@app.route('/Study')
@login_required
def Study():
    Freddy = RandomCard()
    a = Freddy[0]
    b = Freddy[1]
    c = Freddy[2]

    Freddy_Old = RandomCard()
    d = Freddy_Old[0]
    e = Freddy_Old[1]
    f = Freddy_Old[2]

    return render_template("Study.html", First_Card=a, Second_Card=b, Third_Card=c,
                           First_Card_Old=d, Second_Card_Old=e, Third_Card_Old=f, Slovar=Slovar)


@app.route('/Profile', methods=['GET', 'POST'])
@login_required
def user():
    form = Pic()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == session['login']).first()
        try:
            f = form.new_avatar.data
            split_tup = os.path.splitext(f.filename)
            file_extension = split_tup[1]
            filename = f'{str(user.id)}{file_extension}'
            f.save(os.path.join('static/user_pic/', filename))
            user.avatar(user, db_sess, filename)
            session['picture'] = user.picture
        except:
            user.avatar(user, db_sess, 'unnamed.jpg')
            session['picture'] = user.picture
        return render_template('Profile.html', login=session['login'], name=session['name'], picture=session['picture'],
                               form=form)
    return render_template('Profile.html', login=session['login'], name=session['name'], picture=session['picture'],
                           form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# @app.route('/donate')
# @login_required
# def donate():
#     im_donate(session['login'])
#     return redirect("Donate.html")


if __name__ == '__main__':
    db_session.global_init("db/TarAi_Data.db")
    app.run()
