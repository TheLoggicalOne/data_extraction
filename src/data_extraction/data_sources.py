# data_extraction/data_sources.py
class DataSource:
    """Represents a data source, such as a Telegram channel."""
    
    def __init__(self, name, channel_id, description=None):
        self.name = name  # Name of the data source (e.g., channel name)
        self.channel_id = channel_id  # Channel ID or username
        self.description = description  # Optional description of the source

    def __str__(self):
        return f"DataSource(name={self.name}, channel_id={self.channel_id}, description={self.description})"
    