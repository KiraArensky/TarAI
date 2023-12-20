import logging
import os
import random
import string
from datetime import date

try:
    import sqlite3
    import telebot
    from yoomoney import Quickpay
    from yoomoney import Client
except:
    os.system("pip install yoomoney")
    os.system("pip install sqlite3")
    from yoomoney import Quickpay
    from yoomoney import Client
    import sqlite3


def buy_pay(login=None):
    # Подключение к БД
    con = sqlite3.connect("db/TarAi_Data.db")
    # Создание курсора
    cur = con.cursor()

    if not login:
        return 0

    cur.execute(
        f'''INSERT INTO Donate (id, label_for_pay, datetime) VALUES({login}, 'None', '{date.today()}') ''')
    con.commit()

    len_label = 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=len_label))

    quickpay = Quickpay(
        receiver="4100118148718990",
        quickpay_form="shop",
        targets="1 ticket",
        paymentType="SB",
        sum=10000,
        label=str(ran)
    )

    url_donate = quickpay.redirected_url

    cur.execute(f'''UPDATE Donate SET label_for_pay = '{str(ran)}' WHERE id = {login} ''')
    cur.execute(f'''UPDATE Donate SET datetime = '{date.today()}' WHERE id = {login} ''')
    con.commit()
    return url_donate


def im_donate(login):
    # Подключение к БД
    con = sqlite3.connect("db/TarAi_Data.db")
    # Создание курсора
    cur = con.cursor()

    msg = bot.send_message(message.chat.id, text='Идет проверка оплаты')

    token = "4100118148718990.23AB1AE568FAD7B2168C40A500FF7D2ED281C6D6AB911" \
            "1A964CCEA9BB885A8C7D1D0021B95E346FE546CCDCFFC27CEB08210944378C9" \
            "9FDE1B99E82B4ECF7CD14108FAE85D9EB57FE6D4AE43337870EB18496717A13" \
            "1EF9FFC59304254D020B362A0A8B744E40D82940151CA23A6CF69FEE5D5F8F5885EDD862BDE111A8633BC"

    client = Client(token)

    label_pay = cur.execute(f'''SELECT label_for_pay FROM Donate WHERE id = {login}''').fetchone()[0]
    history = client.operation_history(label=label_pay)

    for operation in history.operations:
        if operation.status == "success":
            cur.execute(f'''UPDATE Users SET ticket = '1' WHERE login = {login} ''')
            cur.execute(f'''UPDATE Donate SET label_for_pay = 'None' WHERE id = {login} ''')
            con.commit()
            bot.send_message(message.chat.id, text='Оплата прошла! Спасибо за покупку!')
    else:
        bot.send_message(message.chat.id, text='Упс, оплата не прошла!')
