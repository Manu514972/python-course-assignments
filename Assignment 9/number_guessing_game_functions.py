import random

def generate_secret_number():
    return random.randint(1, 20)

def toggle_debug_mode(debug_mode):
    debug_mode = not debug_mode
    print("Debug mode is now", "ON" if debug_mode else "OFF")
    return debug_mode

def toggle_move_mode(move_mode):
    move_mode = not move_mode
    print("Move mode is now", "ON" if move_mode else "OFF")
    return move_mode

def apply_move_mode(secret_number):
    delta = random.choice([-2, -1, 0, 1, 2])
    secret_number += delta
    return max(1, min(20, secret_number))  

def process_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low")
        return False
    elif guess > secret_number:
        print("Too high")
        return False
    else:
        print("Correct! Starting a new game...")
        return True

def play_game():
    secret_number = generate_secret_number()
    debug_mode = False
    move_mode = False

    print("Welcome to the Number Guessing Game!")

    while True:
        if debug_mode:
            print(f"[DEBUG] Secret number is: {secret_number}")

        user_input = input("Guess a number between 1 and 20 (x = quit, s = show, d = toggle debug, m = toggle move, n = new game): ").lower()

        if user_input == 'x':
            print("You quit the game. Goodbye!")
            break
        elif user_input == 's':
            print(f"The secret number is: {secret_number}")
            continue
        elif user_input == 'd':
            debug_mode = toggle_debug_mode(debug_mode)
            continue
        elif user_input == 'm':
            move_mode = toggle_move_mode(move_mode)
            continue
        elif user_input == 'n':
            secret_number = generate_secret_number()
            print("New game started! A new number has been chosen.")
            continue
        elif not user_input.isdigit():
            print("Please enter a valid number, or use 'x', 's', 'd', 'm', or 'n'.")
            continue

        guess = int(user_input)
        if process_guess(guess, secret_number):
            secret_number = generate_secret_number()
            continue

        if move_mode:
            secret_number = apply_move_mode(secret_number)

if __name__ == "__main__":
    play_game()
