from random import randint

# My free Bingo Generator
status = "a"

def random():
    global list
    list = []
    for i in range(90):
        n = randint(1,90)
        if n not in list:        
            list.append(n)
    return list

def exit():
    print("Bedankt voor het spelen van Bingo!")
    global status
    status = "x"

def output():
    global list
    n = 0
    while n < len(list):
        print(list[n])
        doorgaan = str(input("Druk op 'Enter' of 'q':"))
        if doorgaan == "":
            n = n + 1
        if doorgaan == "q":
            exit()
            break
    else:
        exit()

def shell():
    global status
    while status == "a":
        print("Wilt u de bingo starten: y/n?")
        answer = str(input("y/n?:"))
        
        if answer == "y":
            random()
            output()
        if answer == "n":
            exit()
        else:
            shell()

shell()

