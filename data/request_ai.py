from data.ai_ChatGPT import ai_request


def ai_req(card_1, card_2, card_3, theme):
    request_mess = f'Пожалуйста, проинтерпретируйте значения следующих трех карт Таро: {card_1}, {card_2}, {card_3}.' \
                   f' Раскройте их значения и взаимосвязи, особенно в контексте моей текущей ситуации или вопроса ' \
                   f'о {theme}. Напиши сообщение по такому шаблону: \n"' \
                   f'Туз Жезлов указывает на возможность новых начинаний и энергичного подхода к любовным отношениям. Это может означать, что вам предоставляется шанс создать что-то новое и страстное в своей любовной жизни.' \
                   f'\n\nКолесо Фортуны указывает на изменения в сфере любви. Это может быть как положительным, приносящим удачу и гармонию, так и негативным, требующим адаптации и принятия перемен. В любом случае, эта карта говорит о том, что сейчас наступает новая фаза в вашей любовной жизни.\n\n' \
                   f'2 жезла подчеркивает важность партнерства и сотрудничества в любви. Она может указывать на необходимость поддерживать баланс и гармонию в отношениях, а также на возможность совместного развития и достижения общих целей.' \
                   f'\n\nВ целом, эти карты говорят о возможности начать новое влюбленное партнерство, которое может принести удачу и положительные изменения. Они также подчеркивают важность сотрудничества и взаимного уважения в отношениях. Возможно, сейчас для вас наступает время искать новые возможности в любви и быть готовыми принять перемену. Все это может привести к более гармоничным и удовлетворительным отношениям."'
    ai = ai_request(request_mess).split("\n")
    card_1 = ai[0]
    card_2 = ai[2]
    card_3 = ai[4]
    general_ai = ai[6]
    return card_1, card_2, card_3, general_ai
