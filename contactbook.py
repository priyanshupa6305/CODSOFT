import os

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self, file_path="contacts.txt"):
        self.contacts = []
        self.file_path = file_path
        self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"{contact.name} has been added to the contact book.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n===== Contact List =====")
            for contact in self.contacts:
                print(contact)
            print("========================")

    def search_contact(self, search_term):
        matching_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if matching_contacts:
            print("\nMatching contacts:")
            for contact in matching_contacts:
                print(contact)
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                print(f"Updated phone number for {contact.name}.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"{name} has been deleted from the contact book.")
                return
        print("Contact not found.")

    def save_contacts(self):
        with open(self.file_path, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone},{contact.email},{contact.address}\n")
        print("Contacts saved successfully.")

    def load_contacts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file.readlines():
                    name, phone, email, address = line.strip().split(",")
                    self.contacts.append(Contact(name, phone, email, address))

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")
        print("=============================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term (name or phone): ").strip()
            contact_book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of the contact to update: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            contact_book.update_contact(name, new_phone)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ").strip()
            contact_book.delete_contact(name)
        elif choice == "6":
            contact_book.save_contacts()
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
