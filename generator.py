from random import randint

def random():
    bingo = []
    for i in range(90):
        n = randint(1,90)
        if n not in bingo:        
            bingo.append(n)
    return bingo

#print(random())