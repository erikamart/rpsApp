import e3db
import pickle

##################################
# ROCK PAPER SCISSORS APP
##################################

# Each player can play up to 3 rounds per game.
# They have 3 chances to input the correct move or they automatically lose.
moves = ["rock", "paper", "scissors", "lose"]
rnd = 0
game = 0
a_record_ids = []
b_record_ids = []

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
        #############################################
        # Write an encrypted version of Alicia's move
        # Instantiate Alicia client
        configA = e3db.Config.load("alicia")
        alicia = e3db.Client(configA)

        # Writing a record
        record_type = "a_round" + str(rnd)

        # Create a record by first creating a local version as a dictionary:
        data = {"round": str(rnd), "move": alicia_move, "player": "Alicia"}

        # Now encrypt the *value* part of the record, write it to the server and
        # the server returns the newly created record:
        record = alicia.write(record_type, data)
        record_id = record.meta.record_id
        record_version = record.meta.version

        #########################################
        # Save the record_id to a list for later reading
        a_record_ids.append(record_id)

        # Share the data with Clarence initally and do not stop on error 409 if already shared.
        try:
            # Instantiate third party Client
            configC = e3db.Config.load("clarence")
            clarence = e3db.Client(configC)
            # Share all of the records of type 'a_round#'
            alicia.share(record_type, clarence.client_id)
        except:
            print("")
        finally:
            print("")

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
        #############################################
        # Write an encrypted version of Bruce's move
        # Instantiate Bruce client
        configB = e3db.Config.load("bruce")
        bruce = e3db.Client(configB)

        # Writing a record
        record_type = "b_round" + str(rnd)

        # Create a record by first creating a local version as a dictionary:
        data = {"round": str(rnd), "move": bruce_move, "player": "Bruce"}

        # Now encrypt the *value* part of the record, write it to the server and
        # the server returns the newly created record:
        record = bruce.write(record_type, data)
        record_id = record.meta.record_id
        record_version = record.meta.version

        #########################################
        # Save the record_id to a list for later reading
        b_record_ids.append(record_id)

        # Share the data with Clarence initally and do not stop on error 409 if already shared.
        try:
            # Instantiate third party Client
            configC = e3db.Config.load("clarence")
            clarence = e3db.Client(configC)
            # Share all of the records of type 'b_round#'
            bruce.share(record_type, clarence.client_id)
        except:
            print("")
        finally:
            print("")
    game += 1
else:
    print("\nYou've played 3 rounds and finished this game! Good job!\n")

    # Export Alicia's record_id list data to text file for judge.py
    with open("a_record_ids.txt", "wb") as output:
        pickle.dump(a_record_ids, output)

    # Export Bruce's record_id list data to text file for judge.py
    with open("b_record_ids.txt", "wb") as output:
        pickle.dump(b_record_ids, output)