from random import randint
import os
import time
while True:
    print("Rock, Paper, Scissors")
    print("")
    print("Type 1 For Rock")
    print("Type 2 For Paper")
    print("Type 3 For Scissors")
    Num1 = 0
    try:
        Num1 = int(input("Type a Number:"))
    except ValueError:
        print("")
    Num2 = randint(1, 3)

    if Num1 == 1:
        if Num2 == 1:
            print("The computer chooses Rock!")
            time.sleep(0.5)
            print("You have tied!")
        elif Num2 == 2:
            print("The computer chooses Paper!")
            time.sleep(0.5)
            print("You have lost!")
        elif Num2 == 3:
            print("The computer chooses Scissors!")
            time.sleep(0.5)
            print("You have won!")
    elif Num1 == 2:
        if Num2 == 1:
            print("The computer chooses Rock!")
            time.sleep(0.5)
            print("You have won!")
        elif Num2 == 2:
            print("The computer chooses Paper!")
            time.sleep(0.5)
            print("You have tied!")
        elif Num2 == 3:
            print("The computer chooses Scissors!")
            time.sleep(0.5)
            print("You have lost!")
    elif Num1 == 3:
        if Num2 == 1:
            print("The computer chooses Rock!")
            time.sleep(0.5)
            print("You have lost!")
        elif Num2 == 2:
            print("The computer chooses Paper!")
            time.sleep(0.5)
            print("You have won!")
        elif Num2 == 3:
            print("The computer chooses Scissors!")
            time.sleep(0.5)
            print("You have tied!")
    else:
        print("Please only type 1, 2 or 3")
    time.sleep(2)
    Again = input("Type 1 to play again else type enter")
    if Again == 1
        Again = 0
    else
        break
    os.system('cls')
