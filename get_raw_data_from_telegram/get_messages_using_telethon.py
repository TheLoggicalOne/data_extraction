from telethon import TelegramClient
import os
import json
from datetime import datetime, timedelta

# Replace these with your own values
api_id = os.getenv("TELEGRAM_API_ID")  # Replace with your Telegram API ID
api_hash = os.getenv("TELEGRAM_API_HASH")  # Replace with your Telegram API Hash
channel_username = 'cafekhodroo'  # Replace with the username or ID of the channel
# output_file = 'cafekhodroo_messages_last_120_days.json'  # File to save messages
output_file = 'cafekhodroo_messages_last_1000.json'

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Calculate the date three months ago
four_months_ago = datetime.now() - timedelta(days=120)

async def fetch_messages():
    messages = []
    # Connect to Telegram
    async with client:
        # Get the channel entity
        channel = await client.get_entity(channel_username)
        
        # Fetch messages from the last three months
        async for message in client.iter_messages(channel, limit=1000,
                                                  offset_date=four_months_ago,
                                                  ):
            # Save the message text and additional data
            messages.append({
                'id': message.id,
                'date': str(message.date),
                'text': message.text,
                'sender_id': message.sender_id
            })
        
        # Save messages to a JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)

        print(f"Saved {len(messages)} messages to {output_file}")

# Run the fetch_messages coroutine
client.loop.run_until_complete(fetch_messages())
