import number_guessing_game_functions

def test_generate_secret_number():
    for _ in range(100):
        num = number_guessing_game_functions.generate_secret_number()
        assert 1 <= num <= 20

def test_toggle_debug_mode():
    assert number_guessing_game_functions.toggle_debug_mode(True) is False
    assert number_guessing_game_functions.toggle_debug_mode(False) is True

def test_toggle_move_mode():
    assert number_guessing_game_functions.toggle_move_mode(True) is False
    assert number_guessing_game_functions.toggle_move_mode(False) is True

def test_apply_move_mode():
    for original in range(1, 21):
        new = number_guessing_game_functions.apply_move_mode(original)
        assert 1 <= new <= 20

def test_process_guess_correct(capfd):
    assert number_guessing_game_functions.process_guess(10, 10) is True
    out, _ = capfd.readouterr()
    assert "Correct!" in out

def test_process_guess_too_low(capfd):
    assert number_guessing_game_functions.process_guess(5, 10) is False
    out, _ = capfd.readouterr()
    assert "Too low" in out

def test_process_guess_too_high(capfd):
    assert number_guessing_game_functions.process_guess(15, 10) is False
    out, _ = capfd.readouterr()
    assert "Too high" in out
