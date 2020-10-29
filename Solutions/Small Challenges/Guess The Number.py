import random

starting_lives = 9

print("Guessing Game")
print( f"You only have {starting_lives} lives")
print("You have to guess a number between 1 to 50")

no_of_lives = 0
answer = random.randint(1, 50)

while no_of_lives < 9:
    input_number = int(input("Guess the number: "))
    if input_number < answer:
        print("Oops!, you guessed too low")
        print(f"You have only {starting_lives - no_of_lives} lives left")
    elif input_number > answer:
        print("Oops!, you guessed too high")
        print ( f"You have only {starting_lives - no_of_lives} lives left" )
    else:
        print(f"Congratulations!\nYou guessed the right number in {no_of_lives} tries!")
        break
    no_of_lives += 1
