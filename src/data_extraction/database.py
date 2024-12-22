# data_extraction/database.py
import sqlite3

class Database:
    def __init__(self, db_path="data_extraction.db"):
        self.db_path = db_path
        self._setup_database()

    def _setup_database(self):
        """Set up the database schema if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Create the sources table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS sources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE, NOT NULL,
                type TEXT NOT NULL,           
                identifier TEXT UNIQUE NOT NULL,
                chat_id INTEGER UNIQUE NOT NULL,           
                description TEXT,
                status TEXT DEFAULT 'active',
                metadata TEXT,
                last_fetched TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP                                         
            )
            """)

            # Create the messages table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,
                source_id INTEGER,
                message_id INTEGER,
                sender_id INTEGER,
                text TEXT,
                date TIMESTAMP,
                is_reply BOOLEAN,
                reply_to INTEGER,
                has_image BOOLEAN,
                has_video BOOLEAN,
                has_media BOOLEAN,
                raw_data TEXT,
                FOREIGN KEY (source_id) REFERENCES sources (id),
                UNIQUE(source_id, message_id)
            )
            """)
            conn.commit()

    def save_source(self, name, type_, identifier, chat_id=None, description=None):
        """Save a data source to the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                INSERT OR IGNORE INTO sources (
                    name, type, identifier, chat_id, description
                ) VALUES (?, ?, ?, ?, ?, ?)
                """, (name, type_, identifier, chat_id, description))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    def get_source_id(self, name):
        """Retrieve the source ID for a given name."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT id FROM sources WHERE name = ?
            """, (name,))
            result = cursor.fetchone()
            return result[0] if result else None

    def save_message(self, source_id, message):
        """Save a message to the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                INSERT OR IGNORE INTO messages (
                    source_id, message_id, sender_id, text, date,
                    is_reply, reply_to, has_image, has_video, has_media, raw_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    source_id,
                    message.id,
                    message.from_user.id if message.from_user else None,
                    message.text,
                    message.date,
                    message.reply_to_message_id is not None,
                    message.reply_to_message_id,
                    bool(message.photo),
                    bool(message.video),
                    bool(message.media),
                    str(message)  # Save the raw JSON-like message
                ))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Database error: {e}")
