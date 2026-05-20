from library_service import LibraryService
from exceptions import *

service = LibraryService()

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")

def main():
    while True:
        show_menu()
        try:
            choice = input("Choose an option: ")
            
            if not choice.isdigit():
                raise InvalidInputError("Please enter a number only")
            
            choice = int(choice)
            
            if choice == 1:
                book_id = input("Enter Book ID: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                print(service.add_book(book_id, title, author))
                
            elif choice == 2:
                member_id = input("Enter Member ID: ")
                name = input("Enter Name: ")
                print(service.register_member(member_id, name))
                
            elif choice == 3:
                book_id = input("Enter Book ID: ")
                member_id = input("Enter Member ID: ")
                print(service.borrow_book(book_id, member_id))
                
            elif choice == 4:
                book_id = input("Enter Book ID: ")
                print(service.return_book(book_id))
                
            elif choice == 5:
                print("\n--- All Books ---")
                print(service.view_books())
                
            elif choice == 6:
                print("\n--- All Members ---")
                print(service.view_members())
                
            elif choice == 7:
                print("\n--- All Loans ---")
                print(service.view_loans())
                
            elif choice == 8:
                print("Goodbye!")
                break
                
            else:
                raise InvalidInputError("Invalid menu option. Choose 1-8 only")
                
        except LibraryError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()