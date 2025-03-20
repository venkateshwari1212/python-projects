"""
Develop a Python program to manage a library system
with options to add, remove, and search for books.
"""
library = []

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book = {'title': title, 'author': author}
        library.append(book)
        print(f'Book "{title}" by {author} added successfully.')
    
    elif choice == '2':
        title = input("Enter book title to remove: ")
        found = False
        for book in library:
            if book['title'].lower() == title.lower():
                library.remove(book)
                print(f'Book "{title}" removed successfully.')
                found = True
                break
        if not found:
            print(f'Book "{title}" not found in the library.')
    
    elif choice == '3':
        title = input("Enter book title to search: ")
        found = False
        for book in library:
            if book['title'].lower() == title.lower():
                print(f'Book Found: "{book["title"]}" by {book["author"]}')
                found = True
                break
        if not found:
            print(f'Book "{title}" not found in the library.')
    
    elif choice == '4':
        if not library:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in library:
                print(f'- "{book["title"]}" by {book["author"]}')
    
    elif choice == '5':
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
