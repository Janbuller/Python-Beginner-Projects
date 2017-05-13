from random import randint
import os
import time

tryNumber = 0
print("Name Generator!")
while tryNumber == 0:
    try:
        amount = int(input("How many names do you want to generate?"))
        tryNumber = 1
    except ValueError:
        print("Please only type numbers!")
        time.sleep(2.5)
        os.system('cls')
amountDone = 1
os.system('cls')
firstNames = ("Adam", "Bob", "Tom", "Ellis", "Monet", "Franklyn", "Gwen", "Peter", "Neil", "Leonard", "Howard", "Brian","Penny", "Matthew", "Joe", "Albert", "Jane", "Gordon", "Jack", "Lois", "Kyle", "Kenny", "Steve", "Olivia","Janelle", "Malissa", "Hailey", "Katie", "James", "John", "Robert", "Micheal", "William", "Charles", "David")
lastNames = ("Short", "Harmon", "Jacobson", "Antonyson", "Bullard", "Washington", "Armstrong", "Tash", "Durand","Colbert", "Matthews", "Santoro", "Kennedy", "Swanson", "Smith", "Johnson", "Jones", "Clark", "Jackson","Robinson", "Miller", "Scottson", "Nelson", "Cooper", "Parker", "Adams", "Copeland", "Davenport", "Bruce", "Perry", "Fisher", "Russell")
middleNames = ("James", "Lee", "Micheal", "Joseph", "Alexander", "David", "William", "Andrew", "Matthew", "Robert", "Marie", "Ann", "Rose", "Mae", "Jane", "Thomas", "Nicole", "Lynn", "Grace", "Faith", "Elizabeth", "Renee", "Allen", "Anthony", "Jones")
while amountDone <= amount:
    num1 = randint(1, len(firstNames) - 1)
    num2 = randint(1, len(lastNames) - 1)
    num3 = randint(1, len(middleNames) - 1)
    if firstNames[num1] == middleNames[num3]:
        foo = "foo"
    elif lastNames[num2] == middleNames[num3]:
        bar = "bar"
    else:
        print(firstNames[num1], middleNames[num3], lastNames[num2])
        amountDone += 1
input("Press enter to close")
