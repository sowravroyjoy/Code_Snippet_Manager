import sqlite3

def initialize_database():
    # Connect to SQLite database (or create a new one if it doesn't exist)
    conn = sqlite3.connect('snippets.db')

    # Create a table to store code snippets
    conn.execute('''
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            code TEXT NOT NULL
        )
    ''')

    conn.commit()
    return conn
