import e3db
import pickle

#########################################
# Import winner record_id list data from text file made from judge.py
with open("w_record_ids.txt", "rb") as output:
    w_record_ids = pickle.load(output)

##################################
# Decrypt & read by pulling sever data via imported record_id list

# Instantiate Alicia client
configA = e3db.Config.load("alicia")
alicia = e3db.Client(configA)

# Instantiate Bruce client
configB = e3db.Config.load("bruce")
bruce = e3db.Client(configB)

winners = []
rnd = 1
n = 0
for r in w_record_ids:
    record_id = r
    new_record = bruce.read(record_id)
    win = new_record.data["winner"]
    winners.append(win)
    print('\nRound "' + str(rnd) + '" Winner "' + winners[n] + '"')
    n += 1
    rnd += 1
