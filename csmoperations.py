def add(conn, title, code):
    # adding a new code into the database
    conn.execute('INSERT INTO snippets (title, code) VALUES (?, ?)', (title, code))
    conn.commit()
    print("Snippet added successfully.")

def delete(conn, snippet_id):
    # selecting the coding snippet for deletion
    cursor = conn.execute('SELECT title FROM snippets WHERE id = ?', (snippet_id,))
    row = cursor.fetchone()
    
    if row:
        title = row[0]
        confirm = input(f"Are you sure you want to delete the snippet '{title}'? (yes/no): ").lower()
        
        if confirm == 'yes':
            # deleting the selected code snippet
            conn.execute('DELETE FROM snippets WHERE id = ?', (snippet_id,))
            conn.commit()
            print("Snippet deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Snippet not found.")


def update(conn, snippet_id, new_title=None, new_code=None):
    # selecting the coding snippet for modification
    cursor = conn.execute('SELECT title, code FROM snippets WHERE id = ?', (snippet_id,))
    row = cursor.fetchone()

    if row:
        current_title, current_code = row
        print(f"Current Title: {current_title}\nCurrent Code:\n{current_code}")

        if new_title is None:
            new_title = input("Enter new title (press Enter to keep the current title): ")
            if not new_title:
                new_title = current_title

        if new_code is None:
            new_code = input("Enter new code (press Enter to keep the current code):\n")
            if not new_code:
                new_code = current_code
        # modifying the selected code snippet with new title and code snippet
        conn.execute('UPDATE snippets SET title = ?, code = ? WHERE id = ?', (new_title, new_code, snippet_id))
        conn.commit()
        print("Snippet updated successfully.")
    else:
        print("Snippet not found.")


def view(conn, snippet_id):
    # selecting the coding snippet to display
    cursor = conn.execute('SELECT title, code FROM snippets WHERE id = ?', (snippet_id,))
    row = cursor.fetchone()
    if row:
        print(f"Title: {row[0]}\nCode:\n{row[1]}")
    else:
        print("Snippet not found.")

        
def list(conn):
    # display all saved code snippet
    cursor = conn.execute('SELECT id, title FROM snippets')
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]}")
