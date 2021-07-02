import e3db
import os

# A registration token is required to set up a client. In this situation,
# we assume an environment variable called REGISTRATION_TOKEN is set
token = os.environ.get("REGISTRATION_TOKEN_C")
client_name = "Clarence"

public_key, private_key = e3db.Client.generate_keypair()

# Register the client
client_info = e3db.Client.register(token, client_name, public_key)

# Once the client is registered, use it immediately to create the
# configuration used to instantiate a Client that can communicate with
# e3db directly.
config = e3db.Config(
    client_info.client_id,
    client_info.api_key_id,
    client_info.api_secret,
    public_key,
    private_key,
)

# To save this Configuration to disk
config.write()

# Instantiate your client to communicate with TozStore
client = e3db.Client(config())

# Verify that the configuration was successful
print("Client Id: ", client.client_id)
