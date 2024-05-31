# tg-msg-sender
This script can be useful for sending messages to a specific user or group from multiple Telegram accounts simultaneously. It might be used for various purposes like broadcasting announcements, conducting surveys, or performing other automated tasks on Telegram.

![Screenshot (98)](https://github.com/namokars/tg-msg-sender/assets/82198061/1356bae4-b06a-42c2-8b46-cc25b0b14068)


This Python script utilizes the Telethon library to send messages via Telegram using multiple accounts. Here's a breakdown of what the code does:

1. Import Libraries: The script imports necessary modules from Telethon for interacting with the Telegram API, as well as random and string for generating random messages.

2. API Credentials: API credentials (API ID and API hash) for each Telegram account are defined in lists.

3. Generate Random Message: Random messages are generated using the random and string modules. Two different random messages are generated in this script.

4. Define Target Username: The username of the recipient account where the messages will be sent is specified. Replace 'username' with the actual username.

5. Loop Through Each Account: The script iterates over each Telegram account specified by API ID and API hash.

6. Connect to Telegram API: Inside the loop, a connection to the Telegram API is established using the current account's API credentials.

7. Send Message: A message is sent to the specified username using the SendMessageRequest function from Telethon.

8. Print Status: A message indicating the success of sending the message from each account is printed.
