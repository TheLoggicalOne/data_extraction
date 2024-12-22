# data_extraction/telegram_fetcher.py
import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait
from .database import Database
from .data_sources import DataSource

class TelegramFetcher:
    """Handles fetching messages from Telegram channels."""

    def __init__(self, api_id, api_hash, database):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = Client("telegram_fetcher", api_id=self.api_id, api_hash=self.api_hash)
        self.database = database

    async def fetch_channel_messages(self, data_source, limit=None):
        """
        Fetch all messages from a Telegram channel and save them to the database.

        Args:
            data_source (DataSource): The data source representing the Telegram channel.
            limit (int): Optional limit on the number of messages to fetch (default: None for all).
        """
        print(f"Fetching messages from {data_source}...")
        source_id = self.database.get_source_id(data_source.name)
        if not source_id:
            print(f"Adding new source: {data_source.name}")
            self.database.add_source(data_source.name, data_source.channel_id, data_source.description)
            source_id = self.database.get_source_id(data_source.name)

        messages_fetched = 0
        async with self.client:
            try:
                async for message in self.client.get_chat_history(chat_id=data_source.channel_id, limit=limit):
                    self.database.save_message(source_id, message)
                    messages_fetched += 1

                    # Periodic progress updates
                    if messages_fetched % 100 == 0:
                        print(f"{messages_fetched} messages fetched...")

            except FloodWait as e:
                print(f"Rate limit reached. Waiting for {e.value} seconds...")
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"An error occurred while fetching messages: {e}")

        print(f"Finished fetching messages. Total messages fetched: {messages_fetched}")

    async def close(self):
        """Close the Pyrogram client."""
        await self.client.stop()
