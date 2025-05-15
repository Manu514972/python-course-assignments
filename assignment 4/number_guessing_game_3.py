import random

secret_number = random.randint(1, 20)

while True:
    user_input = input("Guess a number between 1 and 20 (or 'x' to quit, 's' to show the answer): ")

    if user_input.lower() == 'x':
        print("You quit the game. Goodbye!")
        break
    elif user_input.lower() == 's':
        print(f"The secret number is: {secret_number}")
        continue
    elif not user_input.isdigit():
        print("Please enter a valid number, or 'x' to quit, or 's' to cheat.")
        continue

    guess = int(user_input)

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break
