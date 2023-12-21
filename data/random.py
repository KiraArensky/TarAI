import random
import os

def RandomCard():
    List = []
    while len(List)<=3:
        i = random.choice(os.listdir("./ai_test/taro_card_ai"))
        if i in List:
            i = random.choice(os.listdir("./ai_test/taro_card_ai"))
        else:
            List.append(i)

    a = List[0]
    b = List[1]
    c = List[2]
    return [a, b, c]
