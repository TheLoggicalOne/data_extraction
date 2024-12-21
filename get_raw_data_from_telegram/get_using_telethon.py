from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import json
import os

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")

# print(api_id)
# print(api_hash)

output_file = 'cafekhodroo_messages_last_20000.json'



client = TelegramClient('anon', api_id, api_hash)

async def join_channel(client, channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print(f"succesfully joined the channel {channel_link}")
    except:
        print(f"Failed to join the channel {channel_link}")

async def scrape_message(client, channel, limit=100):
    messages = []
    async for message in client.iter_messages(channel, limit):
        
        is_comment = message.reply_to_msg_id is not None
        
        message_data ={
                'id': message.id,
                'date': str(message.date),
                'text': message.text,
                'sender_id': message.sender_id,
                'is_comment': is_comment,
                'is_reply': message.is_reply,
                'related_message_id': message.reply_to_msg_id if is_comment else None
            }
        # if message.text:
        #     print(message.text)
        #     print(40*"-")
            # Save messages to a JSON file

        # Attempt to get sender's username or display name
        if message.sender_id:
            if not message.is_reply:
                sender = await client.get_entity(message.sender_id)
                message_data['sender_name'] = getattr(sender, 'username', getattr(sender, 'title', 'Unknown'))
            else:
                message_data['sender_name'] = 'Not Retrieved'

        else:
            message_data['sender_name'] = 'Unknown'
            
        
        messages.append(message_data)       
    with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)

    print(f"Saved {len(messages)} messages to {output_file}")



async def main():
    # channel_link_to_do= "https://t.me/mahyarkhoodro"
    channel_link_to_do= "https://t.me/cafekhodroo"
    # await join_channel(client, channel_link_to_do)
    
    await scrape_message(client, channel_link_to_do, 20000)

with client: 
    client.loop.run_until_complete(main())