
import random
import os

def RandomCard():
    List = []
    while len(List)<=6:
        i = random.choice(os.listdir("static/tarot_for_Andrey"))
        if i in List:
            i = random.choice(os.listdir("static/tarot_for_Andrey"))
        else:
            List.append(i)

    return List

