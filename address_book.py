"""
AddressBook class - UC2 to UC5, UC7 to UC15
Handles add, edit, delete, search, count, sort, and file operations.
"""

import csv
import json
import os


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """UC2 - Add contact with UC7 duplicate check."""
        for c in self.contacts:
            if c.first_name == contact.first_name and c.last_name == contact.last_name:
                print("Duplicate contact!")
                return False
        self.contacts.append(contact)
        print("Contact added!")
        return True

    def edit_contact(self, name):
        """UC3 - Edit contact by first name."""
        for contact in self.contacts:
            if contact.first_name == name:
                contact.phone = input("Enter new phone: ")
                contact.city = input("Enter new city: ")
                contact.address = input("Enter new address (or press Enter to keep): ") or contact.address
                contact.state = input("Enter new state (or press Enter to keep): ") or contact.state
                contact.zip_code = input("Enter new zip (or press Enter to keep): ") or contact.zip_code
                contact.email = input("Enter new email (or press Enter to keep): ") or contact.email
                contact.last_name = input("Enter new last name (or press Enter to keep): ") or contact.last_name
                print("Contact updated!")
                return True
        print("Contact not found")
        return False

    def delete_contact(self, name):
        """UC4 - Delete contact by first name."""
        for contact in self.contacts:
            if contact.first_name == name:
                self.contacts.remove(contact)
                print("Contact deleted")
                return True
        print("Contact not found")
        return False

    def search_by_city(self, city):
        """UC8 - Search contacts by city."""
        return [c for c in self.contacts if c.city == city]

    def search_by_state(self, state):
        """UC8 - Search contacts by state."""
        return [c for c in self.contacts if c.state == state]

    def count_by_city(self, city):
        """UC10 - Count contacts in a city."""
        return sum(1 for c in self.contacts if c.city == city)

    def count_by_state(self, state):
        """UC10 - Count contacts in a state."""
        return sum(1 for c in self.contacts if c.state == state)

    def sort_by_name(self):
        """UC11 - Sort contacts by first name."""
        return sorted(self.contacts, key=lambda c: (c.first_name, c.last_name))

    def sort_by_city(self):
        """UC12 - Sort contacts by city."""
        return sorted(self.contacts, key=lambda c: c.city)

    def save_to_file(self, filename="contacts.txt"):
        """UC13 - Save contacts to text file."""
        with open(filename, "w") as file:
            for contact in self.contacts:
                file.write(str(contact) + "\n")
        print(f"Saved to {filename}")

    def save_to_csv(self, filename="contacts.csv"):
        """UC14 - Save contacts to CSV file."""
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["first_name", "last_name", "address", "city", "state", "zip_code", "phone", "email"])
            for c in self.contacts:
                writer.writerow([
                    c.first_name, c.last_name, c.address, c.city,
                    c.state, c.zip_code, c.phone, c.email
                ])
        print(f"Saved to {filename}")

    def save_to_json(self, filename="contacts.json"):
        """UC15 - Save contacts to JSON file."""
        data = [c.__dict__ for c in self.contacts]
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Saved to {filename}")

    def load_from_csv(self, filename="contacts.csv"):
        """Load contacts from CSV file."""
        if not os.path.exists(filename):
            return
        from contact import Contact
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                c = Contact(
                    row.get("first_name", ""),
                    row.get("last_name", ""),
                    row.get("address", ""),
                    row.get("city", ""),
                    row.get("state", ""),
                    row.get("zip_code", ""),
                    row.get("phone", ""),
                    row.get("email", "")
                )
                self.contacts.append(c)
        print(f"Loaded from {filename}")

    def load_from_json(self, filename="contacts.json"):
        """Load contacts from JSON file."""
        if not os.path.exists(filename):
            return
        from contact import Contact
        with open(filename, "r") as file:
            data = json.load(file)
            for item in data:
                c = Contact(
                    item.get("first_name", ""),
                    item.get("last_name", ""),
                    item.get("address", ""),
                    item.get("city", ""),
                    item.get("state", ""),
                    item.get("zip_code", ""),
                    item.get("phone", ""),
                    item.get("email", "")
                )
                self.contacts.append(c)
        print(f"Loaded from {filename}")
