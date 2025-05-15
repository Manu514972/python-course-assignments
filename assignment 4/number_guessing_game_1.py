import random

secret_number = random.randint(1, 20)

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break
