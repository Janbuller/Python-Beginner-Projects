from os import system
from time import sleep as slp
print("Addition Calculator")
numList = []
whileLoop1 = 0
while whileLoop1 == 0:
    numList.append(int(input("Please type a number:")))
    system('cls')
    while True:
        nextNumber = input("Do you want to type another number:")
        if nextNumber == "yes" or nextNumber == "Yes" or nextNumber == "YES" or nextNumber == "yEs" or nextNumber == "yeS" or nextNumber == "yES" or nextNumber == "YeS":
            break
        elif nextNumber == "no" or nextNumber == "No" or nextNumber == "nO" or nextNumber == "NO":
            whileLoop1 = 1
            print(sum(numList))
        else:
            print("Please only type Yes or No")
            slp(2.5)
            system('cls')
