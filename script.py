# import asyncio
# from telethon import TelegramClient
# from telethon.errors import SessionPasswordNeededError, FloodWaitError

# # API ID, API Hash, and phone number, get this at me.telegram.org
# api_id = '22865094'
# api_hash = 'ee96e62f21f07702d7c1944f1519f080'
# phone_number = '+2347016407653'

# # The chat ID or username of the user or group i am sending the message to
# chat_id = 'Web_4_vector'  

# # Array of messages to send
# messages = [
#     "Hello!",
#     "How are you today?",
#     "Hope you're doing well!",
#     "Have a great day!",
# ]

# # Create the Telegram client
# client = TelegramClient('session_name', api_id, api_hash)

# async def send_message():
#     try:
#         await client.start(phone_number)  # Start the client and log in
        
#         # Loop through the messages and send each one
#         for i, message in enumerate(messages, start=1):
#             await client.send_message(chat_id, message)
#             print(f"Message {i} sent: {message}")  # Print the message number and content
#             await asyncio.sleep(1)  # Adding a 1-second delay between each message

#     except SessionPasswordNeededError:
#         print("Two-step verification is enabled. Please provide your account password.")
#         password = input("Enter your password: ")
#         await client.start(phone_number, password)
    
#     except FloodWaitError as e:
#         print(f"Flood wait error. Sleeping for {e.seconds} seconds.")
#         await asyncio.sleep(e.seconds)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Run the async function
# with client:
#     client.loop.run_until_complete(send_message())

# # 7016407653

import asyncio
import random
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, FloodWaitError

# API ID, API Hash, and phone number, get this at my.telegram.org
api_id = '22865094'
api_hash = 'ee96e62f21f07702d7c1944f1519f080'
phone_number = '+2347016407653'

# The chat ID or username of the user or group you are sending the message to
chat_id = '4510725869'  

# Array of messages to send
messages = [
    "Hello!",
    "How are you today?",
    "Hope you're doing well!",
    "Have a great day!",
    "Don't forget to smile!",
    "Keep up the great work!",
    "Wishing you all the best!",
    "Take care!",
    "See you soon!",
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
            await asyncio.sleep(random.randint(2, 5))  # Adding a random delay between 2 and 5 seconds

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
