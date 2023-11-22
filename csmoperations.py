def add_snippet(conn, title, code):
    # Insert a new code snippet into the database
    conn.execute('INSERT INTO snippets (title, code) VALUES (?, ?)', (title, code))
    conn.commit()
    print("Snippet added successfully.")

def del_snippet(conn, snippet_id):
    # Insert a new code snippet into the database
    conn.execute('INSERT INTO snippets (title, code) VALUES (?, ?)', (title, code))
    conn.commit()
    print("Snippet added successfully.")

def list_snippets(conn):
    # Retrieve and display all code snippets from the database
    cursor = conn.execute('SELECT id, title FROM snippets')
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]}")

def view_snippet(conn, snippet_id):
    # Retrieve and display a specific code snippet from the database
    cursor = conn.execute('SELECT title, code FROM snippets WHERE id = ?', (snippet_id,))
    row = cursor.fetchone()
    if row:
        print(f"Title: {row[0]}\nCode:\n{row[1]}")
    else:
        print("Snippet not found.")
