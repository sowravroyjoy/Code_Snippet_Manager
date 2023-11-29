"""
copyright 2023
author: Sowrav Roy Joy
This program allows developers to add, delete, 
modify, and view their code which they use frequently.
"""

import csmconnection, csmoperations


if __name__ == "__main__":
    # conecting the database
    con = csmconnection.connection()

    while True:
        print("\n\t WELCOME TO CODE SNIPPET MANAGER - a tool only for developers\n")

        print("1. Copy a snippet")
        print("2. View a snippet")
        print("3. Add a new one manually")
        print("4. Add a new one from a file")
        print("5. Add a existing one to a file")
        print("6. Delete an existing one")
        print("7. Modify an existing one")
        print("8. View all the snippet")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("Enter ID to copy: ")
            csmoperations.copy_clipboard(con, id, csmconnection.pyperclip)
        elif choice == "2":
            id = input("Enter ID to view: ")
            csmoperations.view(con, id)
        elif choice == "3":
            title = input("Enter title: ")
            code = input("Enter code:\n")
            csmoperations.add(con, title, code)
        elif choice == "4":
            file_name = input("Enter filename:\n")
            csmoperations.add_from_file(con, file_name)
        elif choice == "5":
            id = input("Enter ID to copy: ")
            file_name = input("Enter filename:\n")
            csmoperations.copy_to_file(con, file_name, id)
        elif choice == "6":
            id = input("Enter ID to delete: ")
            csmoperations.delete(con, id)
        elif choice == "7":
            id = input("Enter ID to update: ")
            csmoperations.update(con, id)
        elif choice == "8":
            csmoperations.list(con)
        elif choice == "9":
            print("Bye. See you again!!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Closing the database conection
    con.close()
