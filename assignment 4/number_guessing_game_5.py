import random

secret_number = random.randint(1, 20)
debug_mode = False
move_mode = False

while True:
    if debug_mode:
        print(f"[DEBUG] Secret number is: {secret_number}")

    user_input = input("Guess a number between 1 and 20 (x = quit, s = show, d = toggle debug, m = toggle move): ")

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
    elif not user_input.isdigit():
        print("Please enter a valid number, or use 'x', 's', 'd', or 'm'.")
        continue

    guess = int(user_input)

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break

    # Apply Move Mode if it's active
    if move_mode:
        delta = random.choice([-2, -1, 0, 1, 2])
        secret_number += delta
        # Ensure the secret number stays between 1 and 20
        secret_number = max(1, min(20, secret_number))
