

def copy_clipboard(con, id, func):
    # selecting the coding snippet to display
    cursor = con.execute('SELECT title, code FROM snippets WHERE id = ?', (id,))
    row = cursor.fetchone()
    if row:
        func.copy(row[1])
        print(f"Code copied successfully.")
    else:
        print("Not found.")

def view(con, id):
    # selecting the coding snippet to display
    cursor = con.execute('SELECT title, code FROM snippets WHERE id = ?', (id,))
    row = cursor.fetchone()
    if row:
        print(f"Title: {row[0]}\nCode:\n{row[1]}")
    else:
        print("Not found.")

def add(con, title, code):
    # adding a new code into the database
    con.execute('INSERT INTO snippets (title, code) VALUES (?, ?)', (title, code))
    con.commit()
    print("Code added successfully.")

def delete(con, id):
    # selecting the coding snippet for deletion
    cursor = con.execute('SELECT title FROM snippets WHERE id = ?', (id,))
    row = cursor.fetchone()
    
    if row:
        title = row[0]
        confirm = input(f"Are you sure you want to delete the code '{title}'? (yes/no): ").lower()
        
        if confirm == 'yes':
            # deleting the selected code snippet
            con.execute('DELETE FROM snippets WHERE id = ?', (id,))
            con.commit()
            print("Code deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Not found.")

    # Resetting the primary key value to add value after delete any without 
    # skipping the deleted one
    reset_primary_key(con, 'snippets')


def update(con, id, new_title=None, new_code=None):
    # selecting the coding snippet for modification
    cursor = con.execute('SELECT title, code FROM snippets WHERE id = ?', (id,))
    row = cursor.fetchone()

    if row:
        current_title, current_code = row
        print(f"Current Title: {current_title}\nCurrent Code:\n{current_code}")

        if new_title is None:
            new_title = input("Enter new title: ")
            if not new_title:
                new_title = current_title

        if new_code is None:
            new_code = input("Enter new code:\n")
            if not new_code:
                new_code = current_code
        # modifying the selected code snippet with new title and code snippet
        con.execute('UPDATE snippets SET title = ?, code = ? WHERE id = ?', (new_title, new_code, id))
        con.commit()
        print("Code updated successfully.")
    else:
        print("Not found.")

        
def list(con):
    # displaying all saved code snippet
    cursor = con.execute('SELECT id, title FROM snippets')
    isEmpty = True
    for row in cursor.fetchall():
            print(f"{row[0]}. {row[1]}")
            isEmpty = False
    if isEmpty is True:
        print("Table is empty\n")
    
def reset_primary_key(con, table_name):
    # Getting the maximum primary key value
    cursor = con.execute(f'SELECT MAX(id) FROM {table_name}')
    max_id = cursor.fetchone()[0]

    # Resetting the primary key value in sqlite_sequence
    con.execute(f'UPDATE sqlite_sequence SET seq = ? WHERE name = ?', (max_id, table_name))
    con.commit()


def add_from_file(con, filename):
    with open(filename, 'r') as file:
        contents = file.read()

    # adding a new code into the database
    con.execute('INSERT INTO snippets (title, code) VALUES (?, ?)', (filename, contents))
    con.commit()
    print("Code added successfully.")


def copy_to_file(con, filename, id):
    # selecting the coding snippet to display
    cursor = con.execute('SELECT title, code FROM snippets WHERE id = ?', (id,))
    row = cursor.fetchone()
    if row:
        with open(filename, 'a') as file:
            file.write(row[1])
            print(f"Code added successfully to the {filename}.")
    else:
        print("Not found.")


