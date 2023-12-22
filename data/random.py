
import random
import os

def RandomCard():
    List = []
    while len(List)<=3:
        i = random.choice(os.listdir("./ai_test/tarot_for_Andrey"))
        if i in List:
            i = random.choice(os.listdir("./ai_test/tarot_for_Andrey"))
        else:
            List.append(i)

    a = List[0]
    b = List[1]
    c = List[2]
    return [a, b, c]

