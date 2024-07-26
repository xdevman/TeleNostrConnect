import time
from nostr.event import Event, EventKind
from nostr.key import PrivateKey
from nostr.relay_manager import RelayManager

# Your private key (hex string)
private_key_hex = ""
priv_key = PrivateKey.from_hex(private_key_hex)

# Your public key (hex string)
public_key_hex = priv_key.public_key.hex()

# Relay URL
relay_url = "wss://relay.damus.io"

# Create a relay manager and add a relay
relay_manager = RelayManager()
relay_manager.add_relay(relay_url)

# Connect to the relay
relay_manager.open_connections()
time.sleep(1.25)  # allow time for connection to open

# Define the content of your message
message_content = "Hello, Nostr from Python!"

# Create an event
event = Event(
    public_key=public_key_hex,
    content=message_content,
    created_at=int(time.time()),
    kind=EventKind.TEXT_NOTE,
)

# Sign the event
event.sign(priv_key.hex())

# Publish the event
relay_manager.publish_event(event)

# Allow time for message to be sent
time.sleep(1.25)

# Close the connection
relay_manager.close_connections()
