import e3db
import pickle

##################################
# Write & Encrypt, send to server, save record_id in list, and export list to .txt

# Instantiate Alicia client
configA = e3db.Config.load("alicia")
client = e3db.Client(configA)

# Writing a record
record_type = "a_round1"

# Create a record by first creating a local version as a dictionary:
data = {"round": "1", "move": "rock", "player": "Alicia"}

# Now encrypt the *value* part of the record, write it to the server and
# the server returns the newly created record:
record = client.write(record_type, data)
record_id = record.meta.record_id
record_version = record.meta.version

# Save the record_id to a list right after encryption.
# This is for later ability of other clients to read data via unique record_id.
a_record_ids = []
a_record_ids.append(record_id)

# Export Alicia's record_id list data to text file for other clients with access.
with open("a_record_ids.txt", "wb") as output:
    pickle.dump(a_record_ids, output)


##################################
# Sharing by record_type

# Example is if Alicia gave Clarence access to her data

# Instantiate your Client
# Arugment can be changed to alicia, bruce, or clarence as specified in ~/.tozny/
# ~/.tozny/alicia/e3db.json
configA = e3db.Config.load("alicia")
client = e3db.Client(configA)

# Instantiate third party Client
# "third_party" is changed to alicia, bruce, or clarence as specified in ~/.tozny/
configC = e3db.Config.load("clarence")
clarence = e3db.Client(configC)

# Define the list of record_types and loop through each index to share the list
rounds = ["a_round1", "a_round2", "a_round3"]
for r in rounds:
    record_type = r
    # Share all of the records of type 'a_round#' with Clarence's client ID
    client.share(record_type, clarence.client_id)


##################################
# Decrypt & read by pulling sever data via imported record_id list

# Example is for Clarence to access Alicia's data that has been shared with him.

# Import Alicia's record_id list data from text file
with open("a_record_ids.txt", "rb") as output:
    a_record_ids = pickle.load(output)
# print(a_record_ids)

# Instantiate Clarence Client
configC = e3db.Config.load("clarence")
clarence = e3db.Client(configC)

# Use the record's unique ID to read the data and put into another list
alicia_moves = []
for r in a_record_ids:
    record_id = r
    new_record = client.read(record_id)
    a_move = new_record.data["move"]
    alicia_moves.append(a_move)
# print(alicia_moves)
