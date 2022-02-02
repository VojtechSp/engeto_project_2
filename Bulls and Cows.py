import random



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
    generovane_cislo = random.randint(1111, 9999)
    #print(generovane_cislo)
    return generovane_cislo



def hra(cislo):
    predel = "-" * 50
    vyhra = False
    pokusy = 1
    cislo = str(cislo)
    while vyhra == False:
        u_cislo = input()
        if u_cislo.isnumeric() and u_cislo.startswith("0") == False:
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
                    if u_cislo[cifra] in cislo and \
                            u_cislo[cifra] != cislo[cifra]:
                        cows += 1
                print(f"{bulls} bulls, {cows} cows")
                pokusy += 1
                print(predel)
        else:
            print("Please input a number that doesn't start with a 0!")



def main():
    privitani()
    cislo = generovat_cislo()
    hra(cislo)



main()