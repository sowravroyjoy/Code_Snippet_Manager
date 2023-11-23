"""
copyright 2023
author: Sowrav Roy Joy
This program allows developers to add, delete, 
modify, and view their code which they use frequently.
"""

import csmconnection, csmoperations


if __name__ == "__main__":
    # Initializing the database connection
    conn = csmconnection.initialize_database()

    while True:
        print("\n1. View a snippet")
        print("2. Add a new one")
        print("3. Delete an existing one")
        print("4. Modify an existing one")
        print("5. View all the snippet")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            snippet_id = input("Enter snippet ID to view: ")
            csmoperations.view(conn, snippet_id)
        elif choice == "2":
            title = input("Enter snippet title: ")
            code = input("Enter code snippet:\n")
            csmoperations.add(conn, title, code)
        elif choice == "3":
            snippet_id = input("Enter snippet ID to delete: ")
            csmoperations.delete(conn, snippet_id)
        elif choice == "4":
            snippet_id = input("Enter snippet ID to update: ")
            csmoperations.update(conn, snippet_id)
        elif choice == "5":
            csmoperations.list(conn)
        elif choice == "6":
            print("Exiting code snippet manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Closing the database connection
    conn.close()
