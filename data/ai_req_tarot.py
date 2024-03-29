from data.ai_ChatGPT import ai_request


def ai_old_req(cards_tarot, theme):
    card_1, card_2, card_3, card_4, card_5 = map(str, cards_tarot)
    request_mess = f'Пожалуйста, проинтерпретируйте значения следующих пяти карт Таро: {card_1}, {card_2}, {card_3}, {card_4}, {card_5}.' \
                   f' Раскройте их значения и взаимосвязи, особенно в контексте моей текущей ситуации или вопроса ' \
                   f'о {theme}. Напиши сообщение по такому шаблону: \n"' \
                   f'В целом, эти карты говорят о возможности начать новое влюбленное партнерство, которое может принести удачу и положительные изменения. Они также подчеркивают важность сотрудничества и взаимного уважения в отношениях. Возможно, сейчас для вас наступает время искать новые возможности в любви и быть готовыми принять перемену. Все это может привести к более гармоничным и удовлетворительным отношениям."'
    general_ai = ai_request(request_mess)
    return general_ai
