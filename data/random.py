import random
import os
import sqlite3

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
    'Шут.jpg': 'Шут'
}


def RandomCard():
    List = []
    while len(List) <= 6:
        i = random.choice(os.listdir("static/tarot_for_Andrey"))
        if i in List:
            i = random.choice(os.listdir("static/tarot_for_Andrey"))
        else:
            List.append(i)

    return List


