import sqlite3

def connection():
    # connecting to the database or creating it if not exists
    conn = sqlite3.connect('snippets.db')

    # creating a table for storing code snippets
    conn.execute('''
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            code TEXT NOT NULL
        )
    ''')

    conn.commit()
    return conn
