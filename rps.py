#############
# RPS LOGIC

moves = ["rock", "paper", "scissors", "lose"]


def get_win(a, b):

    # Find the lower index of the array that Alicia chose vs.
    # lower index of the array that Bruce chose.
    lower = min(moves.index(a), moves.index(b))
    # Find the higher index of the array that Alicia chose vs.
    # higher index of the array that Bruce chose.
    higher = max(moves.index(a), moves.index(b))

    # Arbitrarily assign players to a lower or higher variable
    lower_player = "Alicia"
    higher_player = "Bruce"
    # Compare moves by player and swap name assignments
    if lower == moves.index(b):
        lower_player = "Bruce"
    if higher == moves.index(a):
        higher_player = "Alicia"
    # Compare indexes and accomodate for players choosing the same or not at all
    if lower == 0 and higher == 2:
        return lower_player
    elif lower == higher <= 2:
        return "everyone"
    elif lower == 3 and higher == 3:
        return "no one"
    elif higher == 3 and lower <= 2:
        return lower_player
    else:
        return higher_player
