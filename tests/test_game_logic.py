from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_go_lower():
    # Bug 2 fix: when guess is too high, message must tell player to go LOWER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Bug 2 fix: when guess is too low, message must tell player to go HIGHER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_secret_always_compared_as_int():
    # Bug 1 fix: guess and secret are both ints — no string comparison side effects
    # "9" > "47" alphabetically but 9 < 47 numerically; correct answer is "Too Low"
    outcome, message = check_guess(9, 47)
    assert outcome == "Too Low"
