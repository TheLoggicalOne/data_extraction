from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import os

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")

# print(api_id)
# print(api_hash)

client = TelegramClient('anon', api_id, api_hash)

async def join_channel(client, channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print(f"succesfully joined the channel {channel_link}")
    except:
        print(f"Failed to join the channel {channel_link}")

async def scrape_message(client, channel, limit=100):
    async for message in client.iter_messages(channel, limit):
        if message.text:
            print(message.stringify())




async def main():
    channel_link_to_do= "https://t.me/mahyarkhoodro"
    await join_channel(client, channel_link_to_do)
    
    await scrape_message(client, channel_link_to_do, 1)

with client: 
    client.loop.run_until_complete(main())