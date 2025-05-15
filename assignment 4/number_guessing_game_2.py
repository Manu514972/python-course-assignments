import random

secret_number = random.randint(1, 20)

while True:
    user_input = input("Guess a number between 1 and 20 (or 'x' to quit): ")
    
    if user_input.lower() == 'x':
        print("You quit the game. Goodbye!")
        break

    if not user_input.isdigit():
        print("Please enter a valid number or 'x' to quit.")
        continue

    guess = int(user_input)

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break
