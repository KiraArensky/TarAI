import pymorphy2
import random
from data.ai_ChatGPT import ai_request


def morph_theme(theme):
    morph = pymorphy2.MorphAnalyzer()

    return morph.parse(theme)[0].inflect({'gent'}).word # Слово в родительный падеж


theme_taro = ["любовь", "здоровье", "карьера", "учеба"] # Список тем гадания
theme = morph_theme(random.choice(theme_taro)) # Рандомная тема в родительном падеже

request_mess = f'Пожалуйста, проинтерпретируйте значения следующих трех карт Таро: {card_1}, {card_2}, {card_3}.' \
                   f' Раскройте их значения и взаимосвязи, особенно в контексте моей текущей ситуации или вопроса ' \
                   f'о {theme}.' # Формулировка запроса для GPT

print(f'Ответ: {ai_request(request_mess)}')  # Вывод ответа
