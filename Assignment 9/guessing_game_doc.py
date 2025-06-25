import random

def generate_secret_number():
    """
    Generates a random secret number between 1 and 20.

    Returns:
        int: A random integer between 1 and 20 (inclusive).

    Example:
    >>> 1 <= generate_secret_number() <= 20
    True
    """
    return random.randint(1, 20)

def toggle_debug_mode(debug_mode):
    """
    Toggles the debug mode flag.

    Args:
        debug_mode (bool): Current state of debug mode.

    Returns:
        bool: Opposite of current state.

    Example:
    >>> toggle_debug_mode(True)
    False
    >>> toggle_debug_mode(False)
    True
    """
    debug_mode = not debug_mode
    print("Debug mode is now", "ON" if debug_mode else "OFF")
    return debug_mode

def toggle_move_mode(move_mode):
    """
    Toggles the move mode flag.

    Args:
        move_mode (bool): Current state of move mode.

    Returns:
        bool: Opposite of current state.

    Example:
    >>> toggle_move_mode(True)
    False
    >>> toggle_move_mode(False)
    True
    """
    move_mode = not move_mode
    print("Move mode is now", "ON" if move_mode else "OFF")
    return move_mode

def apply_move_mode(secret_number):
    """
    Randomly adjusts the secret number by -2 to +2, keeping it within [1, 20].

    Args:
        secret_number (int): Current secret number.

    Returns:
        int: Modified secret number within bounds.

    Example:
    >>> result = apply_move_mode(10)
    >>> 1 <= result <= 20
    True
    """
    delta = random.choice([-2, -1, 0, 1, 2])
    secret_number += delta
    return max(1, min(20, secret_number))

def process_guess(guess, secret_number):
    """
    Compares the guess to the secret number and prints result.

    Args:
        guess (int): The user's guess.
        secret_number (int): The number to guess.

    Returns:
        bool: True if correct, False otherwise.

    Example:
    >>> process_guess(10, 10)
    Correct! Starting a new game...
    True
    >>> process_guess(5, 10)
    Too low
    False
    >>> process_guess(15, 10)
    Too high
    False
    """
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
    import doctest
    doctest.testmod()
    play_game()
