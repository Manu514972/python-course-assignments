import random

def generate_secret_number():
    return random.randint(1, 20)

secret_number = generate_secret_number()
debug_mode = False
move_mode = False

print("Welcome to the Number Guessing Game!")

while True:
    if debug_mode:
        print(f"[DEBUG] Secret number is: {secret_number}")

    user_input = input("Guess a number between 1 and 20 (x = quit, s = show, d = toggle debug, m = toggle move, n = new game): ")

    if user_input.lower() == 'x':
        print("You quit the game. Goodbye!")
        break
    elif user_input.lower() == 's':
        print(f"The secret number is: {secret_number}")
        continue
    elif user_input.lower() == 'd':
        debug_mode = not debug_mode
        print("Debug mode is now", "ON" if debug_mode else "OFF")
        continue
    elif user_input.lower() == 'm':
        move_mode = not move_mode
        print("Move mode is now", "ON" if move_mode else "OFF")
        continue
    elif user_input.lower() == 'n':
        secret_number = generate_secret_number()
        print("New game started! A new number has been chosen.")
        continue
    elif not user_input.isdigit():
        print("Please enter a valid number, or use 'x', 's', 'd', 'm', or 'n'.")
        continue

    guess = int(user_input)

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct! Starting a new game...")
        secret_number = generate_secret_number()
        continue

    # Apply Move Mode if it's active
    if move_mode:
        delta = random.choice([-2, -1, 0, 1, 2])
        secret_number += delta
        secret_number = max(1, min(20, secret_number))  # keep within bounds
