import e3db
import pickle
import rps

#########################################
# Import Alicia's record_id list data from text file made from play.py
with open("a_record_ids.txt", "rb") as output:
    a_record_ids = pickle.load(output)

# Import Bruce's record_id list data from text file made from play.py
with open("b_record_ids.txt", "rb") as output:
    b_record_ids = pickle.load(output)

#############################################
# Clarence decrypts to read the encrypted data for the players based on record_id

# Instantiate Clarence Client
configC = e3db.Config.load("clarence")
clarence = e3db.Client(configC)

# Use the record's unique record ID to read the data and put into a list
alicia_moves = []
for r in a_record_ids:
    record_id = r
    new_record = clarence.read(record_id)
    a_move = new_record.data["move"]
    alicia_moves.append(a_move)

bruce_moves = []
for r in b_record_ids:
    record_id = r
    new_record = clarence.read(record_id)
    b_move = new_record.data["move"]
    bruce_moves.append(b_move)

# Index the moves lists to find the winner of each round and put them in another list
alicia_move = alicia_moves
bruce_move = bruce_moves
win = []
for i in range(3):
    winners = rps.get_win(alicia_move[i], bruce_move[i])
    win.append(winners)

#############################################
# Write an encrypted version of winners for each round.
# Save the record_id in a list as they are created.
# Share the record_type with the players as they are made.
rnd = 1
n = 0
w_record_ids = []

for w in range(3):
    # Writing a record
    record_type = "winners" + str(rnd)

    # Create a record by first creating a local version as a dictionary:
    data = {"round": str(rnd), "winner": win[n]}

    # Print that the round has been judged
    print('\nRound "' + str(rnd) + '" Judged!')

    # Now encrypt the *value* part of the record, write it to the server and
    # the server returns the newly created record:
    record = clarence.write(record_type, data)
    record_id = record.meta.record_id
    record_version = record.meta.version

    #########################################
    # Save the record_id to a list for later reading
    w_record_ids.append(record_id)

    rnd += 1
    n += 1

# Export w_record_ids list data to text file for winner.py
with open("w_record_ids.txt", "wb") as output:
    pickle.dump(w_record_ids, output)