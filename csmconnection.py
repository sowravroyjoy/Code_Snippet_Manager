import sqlite3, pyperclip

def connection():
    # conecting to the database or creating it if not exists
    con = sqlite3.connect('snippets.db')


    tSql = '''
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            code TEXT NOT NULL
        )
    '''
    # creating a table for storing code snippets
    con.execute(tSql)

    con.commit()
    return con
