##################################
# Rock Paper Scissors Logic

moves = ["rock", "paper", "scissors", "lose"]


def get_winner(a, b):

    # Find the lower index of the array that Alicia chose vs. lower index of the array that Bruce chose.
    lower = min(moves.index(a), moves.index(b))
    # Find the higher index of the array that Alicia chose vs. higher index of the array that Bruce chose.
    higher = max(moves.index(a), moves.index(b))

    lower_player = "Alicia"
    higher_player = "Bruce"
    if lower == moves.index(b):
        lower_player = "Bruce"
    if higher == moves.index(a):
        higher_player = "Alicia"

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


##################################
# Games

rnd = 0
game = 0
while game < 3:
    counter = 0
    alicia_move = input("\nAlicia, enter your move...\n")
    while alicia_move not in moves and counter < 3:
        print("Invalid choice! Try again!")
        alicia_move = input("Alicia, enter your move...\n")
        counter += 1
        if counter == 2:
            rnd += 1
            print("You lose!")
            alicia_move = "lose"
            break
    else:
        rnd += 1
        print(
            'Round "'
            + str(rnd)
            + '" Move "'
            + alicia_move.capitalize()
            + '" for "Alicia" submitted!\n'
        )
        clarence_a = 'Round "' + str(rnd) + '" Move "' + alicia_move.capitalize()

    counter = 0
    bruce_move = input("Bruce, enter your move...\n")
    while bruce_move not in moves and counter < 3:
        print("Invalid choice! Try again!")
        bruce_move = input("Bruce, enter your move...\n")
        counter += 1
        if counter == 2:
            print("You lose!")
            bruce_move = "lose"
            break
    else:
        print(
            'Round "'
            + str(rnd)
            + '" Move "'
            + bruce_move.capitalize()
            + '" for "Bruce" submitted!\n'
        )
        clarence_b = 'Round "' + str(rnd) + '" Move "' + bruce_move.capitalize()

    winner = get_winner(alicia_move, bruce_move)
    game += 1
    print("winner: " + winner + "!\n")
else:
    print("\nYou've played 3 rounds and finished this game! Good job!\n")
