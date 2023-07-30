from generator import *
from exit import *
# My free Bingo Generator
bingo = random()
status = "a"

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
            status = "x"
        else:
            shell()

def output():
    global status
    n = 0
    while n < (len(bingo)-1):
        print(bingo[n])
        doorgaan = str(input("Doorgaan? Druk op 'Enter', b, of 'q':"))
        
        if doorgaan == "b":
            print("Dit zijn de getrokken getallen:")
            print(bingo[:(n+1)])
        if doorgaan == "q":
            exit()
            status = "x"
            break
        if doorgaan == "":
            n = n + 1
    else:
        print("Dit waren alle getallen van links naar rechts:")
        columns = 9
        for a, b, c, d, e, f, g, h, i in zip(bingo[::columns], bingo[1::columns], bingo[2::columns], bingo[3::columns],
        bingo[4::columns], bingo[5::columns], bingo[6::columns], bingo[7::columns], bingo[8::columns]):
            print(f'{a: <10}{b: <10}{c: <10}{d: <10}{e: <10}{f: <10}{g: <10}{h: <10}{i}')
        exit()
        status = "x"

shell()