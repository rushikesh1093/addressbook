"""
AddressBookSystem - UC6
Manages multiple address books.
"""

from address_book import AddressBook


class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def create_book(self, name):
        """Create a new address book with the given name."""
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
            return False
        self.address_books[name] = AddressBook()
        print(f"Address book '{name}' created.")
        return True

    def get_book(self, name):
        """Get an address book by name."""
        return self.address_books.get(name)

    def list_books(self):
        """Return list of address book names."""
        return list(self.address_books.keys())

    def delete_book(self, name):
        """Remove an address book."""
        if name in self.address_books:
            del self.address_books[name]
            print(f"Address book '{name}' deleted.")
            return True
        print(f"Address book '{name}' not found.")
        return False
