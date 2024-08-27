import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, FloodWaitError

# API ID, API Hash, and phone number, get this at me.telegram.org
api_id = '28155213'
api_hash = '64d4c3fe407787fe9dfa8f34d46268ba'
phone_number = '+2349151010600'

# The chat ID or username of the user or group i am sending the message to
chat_id = 'Stacy_kello'  

# Array of messages to send
messages = [
    "Hello!",
    "How are you today?",
    "Here's a random sentence.",
    "This is a test message.",
    "Hope you're doing well!",
    "Check out this cool feature!",
    "Have a great day!",
    "Here's some more text.",
    "Just sending a message.",
    "Last message in the list."
]

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def send_message():
    try:
        await client.start(phone_number)  # Start the client and log in
        
        # Loop through the messages and send each one
        for i, message in enumerate(messages, start=1):
            await client.send_message(chat_id, message)
            print(f"Message {i} sent: {message}")  # Print the message number and content
            await asyncio.sleep(1)  # Adding a 1-second delay between each message

    except SessionPasswordNeededError:
        print("Two-step verification is enabled. Please provide your account password.")
        password = input("Enter your password: ")
        await client.start(phone_number, password)
    
    except FloodWaitError as e:
        print(f"Flood wait error. Sleeping for {e.seconds} seconds.")
        await asyncio.sleep(e.seconds)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the async function
with client:
    client.loop.run_until_complete(send_message())
