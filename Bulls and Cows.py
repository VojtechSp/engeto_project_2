import random

predel = "-" * 50

def privitani():
    predel = "-" * 50
    print(f"Hi there!\n"
          f"{predel}\n"
          f"I've generated a random 4 digit number for you.\n"
          f"Let's play a bulls and cows game.\n"
          f"{predel}\n"
          f"Enter a number:\n"
          f"{predel}")



def generovat_cislo():
    generovane_cislo = []
    while len(generovane_cislo) < 4:
        temp = str(random.randint(0, 9))
        if temp not in generovane_cislo and int(temp) != 0:
            generovane_cislo.append(temp)

    #print(generovane_cislo)
    return "".join(generovane_cislo)

def zkontrolovat_cislo(cislo : str):
    if cislo.isnumeric():
        if not cislo.startswith('0'):
            if len(cislo) == 4:
                for x in cislo:
                    if cislo.count(x) == 1:
                        continue
                    else:
                        print("There are repeating numbers in your input!")
                        return False
                return True
            elif len(cislo) < 4:
                print("Number input is too short!")
                return False
            else:
                print("Number input is too long!")
                return False
        else:
            print("Please input a number that doesn't start with a 0!")
            return False
    else:
        print("input a NUMBER!")
        return False



def hra(cislo):
    vyhra = False
    pokusy = 1
    cislo = str(cislo)
    while vyhra == False:
        u_cislo = input()
        kontrola = zkontrolovat_cislo(u_cislo)
        if kontrola:
            if u_cislo == cislo:
                print(f"Correct, you've guessed the right number\n"
                        f"in {pokusy} guesses!\n"
                        f"{predel}")
                vyhra = True
            else:
                bulls = 0
                cows = 0
                for cifra in range(4):
                    if u_cislo[cifra] == cislo[cifra]:
                        bulls += 1
                for cifra in range(4):
                    if u_cislo[cifra] in cislo and u_cislo[cifra] != cislo[cifra]:
                        cows += 1
                print(f"{bulls} bulls, {cows} cows")
                pokusy += 1
                print(predel)


def main():
    privitani()
    cislo = generovat_cislo()
    hra(cislo)



main()