from backend import Book, Library

def print_books(books):
    if not books:
        print("No books found.")
        return
    print("\nID\tTitle\tAuthor\tQuantity")
    print("-" * 40)
    for b in books:
        print(f"{b.book_id}\t{b.title}\t{b.author}\t{b.quantity}")

def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            try:
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Quantity must be a number!")
                continue

            book = Book(book_id, title, author, quantity)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == "2":
            books = library.view_books()
            print_books(books)

        elif choice == "3":
            keyword = input("Enter ID/Title/Author to search: ")
            result = library.search_book(keyword)
            print_books(result)

        elif choice == "4":
            book_id = input("Enter Book ID to issue: ")
            success, msg = library.issue_book(book_id)
            print(msg)

        elif choice == "5":
            book_id = input("Enter Book ID to return: ")
            success, msg = library.return_book(book_id)
            print(msg)

        elif choice == "6":
            print("Exiting... Data saved.")
            break

        else:
            print("Invalid choice. Try again.")

# THIS PART IS VERY IMPORTANT
if __name__ == "__main__":
    main()
