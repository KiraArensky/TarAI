import os
from flask import *
from sqlite3 import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data.picform import Pic
from data.random import RandomCard
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

Slovar = {
        '2жезла.jpg': '2 жезла',
        '2мечей.jpg': '2 меча',
        '2пентаклей.jpg': '2 пентакли',
        '2чаши.jpg': '2 чаши',

        '3жезла.jpg': '3 жезла',
        '3меча.jpg': '3 меча',
        '3пентаклей.jpg': '3 пентакли',
        '3чаш.jpg': '3 чаши',

        '4жезла.jpg': '4 жезла',
        '4меча.jpg': '4 меча',
        '4пентаклей.jpg': '4 пентакли',
        '4чаши.jpg': '4 чаши',

        '5жезлов.jpg': '5 жезлов',
        '5мечей.jpg': '5 мечей',
        '5пентаклей.jpg': '5 пентаклей',
        '5чаш.jpg': '5 чаш',

        '6жезлов.jpg': '6 жезлов',
        '6мечей.jpg': '6 мечей',
        '6пентаклей.jpg': '6 пентаклей',
        '6чаш.jpg': '6 чаш',

        '7жезлов.jpg': '7 жезлов',
        '7мечей.jpg': '7 мечей',
        '7пентаклей.jpg': '7 пентаклей',
        '7чаш.jpg': '7 чаш',

        '8жезлов.jpg': '8 жезлов',
        '8мечей.jpg': '8 мечей',
        '8пентаклей.jpg': '8 пентаклей',
        '8чаш.jpg': '8 чаш',

        '9жезлов.jpg': '9 жезлов',
        '9мечей.jpg': '9 мечей',
        '9пентаклей.jpg': '9 пентаклей',
        '9чаш.jpg': '9 чаш',

        '10жезлов.jpg': '10 жезлов',
        '10мечей.jpg': '10 мечей',
        '10пентаклей.jpg': '10 пентаклей',
        '10чаш.jpg': '10 чаш',

        'Башня.jpg': 'Башня',
        'Влюбленные.jpg': 'Влюбленные',
        'Дьявол.jpg': 'Дьявол',
        'Жрица.jpg': 'Жрица',
        'Звезда.jpg': 'Звезда',
        'Император.jpg': 'Император',
        'Императрица.jpg': 'Императрица',
        'Колесница.jpg': 'Колесница',
        'КолесоФортуны.jpg': 'Колесо Фортуны',
        'КоролеваЖезлов.jpg': 'Королева Жезлов',
        'КоролеваМечей.jpg': 'Королева Мечей',
        'КоролеваПентаклей.jpg': 'Королева Пентаклей',
        'КоролеваЧаш.jpg': 'Королева Чаш',
        'КорольЖезлов.jpg': 'Король Жезлов',
        'КорольМечей.jpg': 'Король Мечей',
        'КорольПентаклей.jpg': 'Король Пентаклей',
        'КорольЧаш.jpg': 'Король Чаш',
        'Луна.jpg': 'Луна',
        'Маг.jpg': 'Маг',
        'Мир.jpg': 'Мир',
        'Отшельник.jpg': 'Отшельник',
        'ПажЖезлов.jpg': 'Паж Жезлов',
        'ПажМечей.jpg': 'Паж Мечей',
        'ПажПентаклей.jpg': 'Паж Пентаклей',
        'ПажЧаш.jpg': 'Паж Чаш',
        'ПервосвященникИерофант.jpg': 'Первосвященник Иерофант',
        'Повешенный.jpg': 'Повешенный',
        'Правосудие.jpg': 'Правосудие',
        'РыцарьЖезлов.jpg': 'Рыцарь Жезлов',
        'РыцарьМечей.jpg': 'Рыцарь Мечей',
        'РыцарьПентаклей.jpg': 'Рыцарь Пентаклей',
        'РыцарьЧаш.jpg': 'Рыцарь Чаш',
        'Сила.jpg': 'Сила',
        'Смерть.jpg': 'Смерть',
        'Солнце.jpg': 'Солнце',
        'СтрашныйСуд.jpg': 'Страшный Суд',
        'ТузЖезлов.jpg': 'Туз Жезлов',
        'ТузМечей.jpg': 'Туз Мечей',
        'ТузПентаклей.jpg': 'Туз Пентаклей',
        'ТузЧаш.jpg': 'ТузЧаш',
        'Умеренность.jpg': 'Умеренность',
        'Шут.jpg': 'Шут',

    }

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

@app.route('/Profile')
@login_required
def user():
    form = Pic()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == session['login']).first()
        try:
            f = request.files['picture']
            print(1)
            split_tup = os.path.splitext(f.filename)
            print(2)
            file_extension = split_tup[1]
            print(4)

            filename = f'{str(user.id)}{file_extension}'
            print(5)

            f.save(os.path.join('static/user_pic/', filename))
            print(6)

            user.avatar(user, db_sess, filename)
            print(7)

            session['picture'] = user.picture
            print(session)
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




if __name__ == '__main__':
    db_session.global_init("db/TarAi_Data.db")
    app.run()
