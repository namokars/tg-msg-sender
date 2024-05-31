from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
import random
import string

# Define API credentials for the accounts
api_ids = ['YOUR_API_ID', 'YOUR_API_ID2']
api_hashes = ['HASH', 'HASH2']

# Generate a random message
random_message = 'MESSAGE'

# Define the username to send the message to
username = 'username'

# Loop through each account
for api_id, api_hash in zip(api_ids, api_hashes):
    # Connect the Telegram account to the Telegram API
    with TelegramClient(f'session_name_{api_id}', api_id, api_hash) as client:
        # Log in to the account
        client.start()

        # Send a message to the specified username
        client(SendMessageRequest(username, random_message))

        print(f"Message sent from account with API ID {api_id} to {username}. Task Done.")
