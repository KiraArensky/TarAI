import logging
import os
import random
import string
import time
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
    import telebot
    import sqlite3


def buy_p18_pay(message):
    # Подключение к БД
    con = sqlite3.connect("database/chats.db")
    # Создание курсора
    cur = con.cursor()

    result = cur.execute("""SELECT id FROM p18""").fetchall()
    id_list = [elem[0] for elem in result]

    len_label = 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=len_label))

    old_chec = cur.execute(f'''SELECT chec FROM p18 WHERE id = {message.chat.id}''').fetchone()[0]

    quickpay = Quickpay(
        receiver="4100118148718990",
        quickpay_form="shop",
        targets="subscribe to p18",
        paymentType="SB",
        sum=150,
        label=str(ran)
    )

    chec1 = quickpay.redirected_url

    cur.execute(f'''UPDATE p18 SET label_for_pay = '{str(ran)}' WHERE id = {message.chat.id} ''')
    cur.execute(f'''UPDATE p18 SET datetime = '{date.today()}' WHERE id = {message.chat.id} ''')
    con.commit()

    chec2 = bot.send_message(message.chat.id, text='После перевода сохраните скриншот об оплате '
                                                   'и введите /im_buy_p18\n\n')

    chec = f'{chec1.id} {chec2.id}'
    cur.execute(f'''UPDATE p18 SET chec = '{chec}' WHERE id = {message.chat.id} ''')
    con.commit()


@bot.message_handler(commands=['im_buy_p18'])
def im_buy_p18(message):
    # Подключение к БД
    con = sqlite3.connect("database/chats.db")
    # Создание курсора
    cur = con.cursor()

    try:
        old_msg = cur.execute(f'''SELECT chec FROM p18 WHERE id = {message.chat.id}''').fetchone()[0]
        old_msg = old_msg.split()
        bot.delete_message(message.chat.id, int(old_msg[0]))
        bot.delete_message(message.chat.id, int(old_msg[1]))
    except telebot.apihelper.ApiTelegramException:
        pass

    msg = bot.send_message(message.chat.id, text='Идет проверка оплаты')

    token = "4100118148718990.23AB1AE568FAD7B2168C40A500FF7D2ED281C6D6AB911" \
            "1A964CCEA9BB885A8C7D1D0021B95E346FE546CCDCFFC27CEB08210944378C9" \
            "9FDE1B99E82B4ECF7CD14108FAE85D9EB57FE6D4AE43337870EB18496717A13" \
            "1EF9FFC59304254D020B362A0A8B744E40D82940151CA23A6CF69FEE5D5F8F5885EDD862BDE111A8633BC"
    client = Client(token)

    label_pay = cur.execute(f'''SELECT label_for_pay FROM p18 WHERE id = {message.chat.id}''').fetchone()[0]
    history = client.operation_history(label=label_pay)

    for operation in history.operations:
        if operation.status == "success":
            cur.execute(f'''UPDATE id SET p18 = True WHERE id = {message.chat.id} ''')
            cur.execute(f'''UPDATE id SET date_p18 = '{operation.datetime.date()}' WHERE id = {message.chat.id} ''')
            cur.execute(f'''UPDATE p18 SET label_for_pay = 'None' WHERE id = {message.chat.id} ''')
            con.commit()
            bot.delete_message(message.chat.id, msg.id)
            bot.send_message(message.chat.id, text='Оплата прошла! Спасибо за покупку!')
    else:
        bot.delete_message(message.chat.id, msg.id)
        bot.send_message(message.chat.id, text='Упс, оплата не прошла!')
