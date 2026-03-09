"""
Address Book System - Main Program
UC1 to UC15: Contact, AddressBook, Multiple Books, Search, Count, Sort, File I/O
"""

from contact import Contact
from address_book import AddressBook
from system import AddressBookSystem


def get_current_book(system):
    """Get current address book; create default if none exists."""
    if not system.address_books:
        system.create_book("default")
    return system.get_book("default")


def add_contact_flow(book):
    """Gather contact details and add to book."""
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    address = input("Address: ").strip()
    city = input("City: ").strip()
    state = input("State: ").strip()
    zip_code = input("Zip code: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    c = Contact(first, last, address, city, state, zip_code, phone, email)
    book.add_contact(c)


def edit_contact_flow(book):
    """Edit contact by first name."""
    name = input("Enter first name of contact to edit: ").strip()
    book.edit_contact(name)


def delete_contact_flow(book):
    """Delete contact by first name."""
    name = input("Enter first name of contact to delete: ").strip()
    book.delete_contact(name)


def display_contacts(book, contacts=None):
    """Display list of contacts."""
    to_show = contacts if contacts is not None else book.contacts
    if not to_show:
        print("No contacts.")
        return
    for c in to_show:
        print(c)


def search_flow(book):
    """UC8 - Search by city or state."""
    print("1. Search by city  2. Search by state")
    ch = input("Choice: ").strip()
    if ch == "1":
        city = input("City: ").strip()
        result = book.search_by_city(city)
        print(f"Found {len(result)} contact(s):")
        display_contacts(book, result)
    elif ch == "2":
        state = input("State: ").strip()
        result = book.search_by_state(state)
        print(f"Found {len(result)} contact(s):")
        display_contacts(book, result)
    else:
        print("Invalid choice.")


def count_flow(book):
    """UC10 - Count by city or state."""
    print("1. Count by city  2. Count by state")
    ch = input("Choice: ").strip()
    if ch == "1":
        city = input("City: ").strip()
        print(f"Count: {book.count_by_city(city)}")
    elif ch == "2":
        state = input("State: ").strip()
        print(f"Count: {book.count_by_state(state)}")
    else:
        print("Invalid choice.")


def sort_flow(book):
    """UC11 & UC12 - Sort by name or city."""
    print("1. Sort by name  2. Sort by city")
    ch = input("Choice: ").strip()
    if ch == "1":
        display_contacts(book, book.sort_by_name())
    elif ch == "2":
        display_contacts(book, book.sort_by_city())
    else:
        print("Invalid choice.")


def file_flow(book):
    """UC13, UC14, UC15 - Save to txt, CSV, or JSON."""
    print("1. Save to TXT  2. Save to CSV  3. Save to JSON  4. Load from CSV  5. Load from JSON")
    ch = input("Choice: ").strip()
    if ch == "1":
        book.save_to_file("contacts.txt")
    elif ch == "2":
        book.save_to_csv("contacts.csv")
    elif ch == "3":
        book.save_to_json("contacts.json")
    elif ch == "4":
        book.load_from_csv("contacts.csv")
    elif ch == "5":
        book.load_from_json("contacts.json")
    else:
        print("Invalid choice.")


def main():
    system = AddressBookSystem()
    book = get_current_book(system)

    while True:
        print("\n--- Address Book ---")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Search by City/State (UC8)")
        print("6. Count by City/State (UC10)")
        print("7. Sort by Name/City (UC11/12)")
        print("8. Save/Load (TXT, CSV, JSON)")
        print("9. Multiple Books: Create/Switch/List")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_contact_flow(book)
        elif choice == "2":
            edit_contact_flow(book)
        elif choice == "3":
            delete_contact_flow(book)
        elif choice == "4":
            display_contacts(book)
        elif choice == "5":
            search_flow(book)
        elif choice == "6":
            count_flow(book)
        elif choice == "7":
            sort_flow(book)
        elif choice == "8":
            file_flow(book)
        elif choice == "9":
            print("1. Create book  2. Switch book  3. List books")
            sub = input("Choice: ").strip()
            if sub == "1":
                name = input("Book name: ").strip()
                system.create_book(name)
            elif sub == "2":
                names = system.list_books()
                if not names:
                    print("No books.")
                    continue
                print("Books:", ", ".join(names))
                name = input("Switch to book: ").strip()
                b = system.get_book(name)
                if b:
                    book = b
                    print(f"Using book: {name}")
                else:
                    print("Book not found.")
            elif sub == "3":
                print("Books:", system.list_books() or "None")
            else:
                print("Invalid choice.")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
