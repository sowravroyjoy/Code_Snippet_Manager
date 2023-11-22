from csmconnection import initialize_database
from csmoperations import add_snippet, list_snippets, view_snippet

def main():
    # Initialize the database connection
    conn = initialize_database()

    while True:
        print("\n1. Add a snippet")
        print("2. List all snippets")
        print("3. View a snippet")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter snippet title: ")
            code = input("Enter code snippet:\n")
            add_snippet(conn, title, code)
        elif choice == "2":
            list_snippets(conn)
        elif choice == "3":
            snippet_id = input("Enter snippet ID to view: ")
            view_snippet(conn, snippet_id)
        elif choice == "4":
            print("Exiting snippet manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection when the program exits
    conn.close()

if __name__ == "__main__":
    main()
