import random

print("Guessing Game")
print("You have only 9 lives")
print("You have to guess only from 1 to 50")

no_of_lives = 0
answer = random.randint(1, 50)

while no_of_lives < 9:
    input_number = int(input("Guess the number: "))
    if input_number < answer:
        print("Oops!, you guessed too less")
        print(f"You have only {9 - no_of_lives} number of lives")
    elif input_number > answer:
        print("Oops!, you guessed too high")
        print ( f"You have only {9 - no_of_lives} number of lives" )
    else:
        print(f"Congratulations!, you guessed the right number in {no_of_lives} number of lives")
        break
    no_of_lives += 1
