from random import randint

# My free Bingo Generator
status = 1

def shell():
    global status
    while status == 1:
        print("Wilt u de bingo starten: j/n?")
        answer = str(input("j/n?:"))
        if answer == "j":
            random()
            output()
        if answer == "n":
            exit()
            status = 0
        else:
            shell()

def random():
    global bingo
    bingo = []
    for i in range(90):
        n = randint(1,90)
        if n not in bingo:        
            bingo.append(n)
    return bingo

def output():
    n = 0
    while n < (len(bingo)-1):
        print(bingo[n])
        doorgaan = str(input("Doorgaan? Druk op 'Enter', b, of 'q':"))
    
        if doorgaan == "b":
            print("Dit zijn de getrokken getallen:")
            print(bingo[:(n+1)])
        if doorgaan == "q":
            exit()
            break
        else:
            n = n + 1
    else:
        print("Dit waren alle getallen van links naar rechts:")
        columns = 9
        for a, b, c, d, e, f, g, h, i in zip(bingo[::columns], bingo[1::columns], bingo[2::columns], bingo[3::columns],
        bingo[4::columns], bingo[5::columns], bingo[6::columns], bingo[7::columns], bingo[8::columns]):
            print(f'{a: <10}{b: <10}{c: <10}{d: <10}{e: <10}{f: <10}{g: <10}{h: <10}{i}')
        exit()

def exit():
    global status
    status = 0
    print("Bedankt voor het spelen van Bingo!")

shell()