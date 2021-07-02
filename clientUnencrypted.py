import e3db

################################
# Test Write Unencrypted data by sending inital contact info for each client

# Instantiate your Client
# Arg can be alicia, bruce, or clarence directories as specified in ~/.tozny/
# Directory name used as an arg will default to this file path: ~/.tozny/alicia/e3db.json
configA = e3db.Config.load("alicia")
client = e3db.Client(configA)

record_type = "contact"
data = {"first_name": "Alicia", "last_name": "Player1", "phone": "888-867-5309"}

metadata = {"player": "1"}

record = client.write(record_type, data, metadata)


#################
# Bruce Contact

configB = e3db.Config.load("bruce")
bruce = e3db.Client(configB)

record_type = "contact"
data = {"first_name": "Bruce", "last_name": "Player2", "phone": "888-555-5555"}

metadata = {"player": "2"}

record = bruce.write(record_type, data, metadata)


#################
# Clarence Contact

configC = e3db.Config.load("clarence")
clarence = e3db.Client(configC)

record_type = "contact"
data = {"first_name": "Clarence", "last_name": "Judge", "phone": "888-888-8888"}

metadata = {"judge": "1"}

record = clarence.write(record_type, data, metadata)