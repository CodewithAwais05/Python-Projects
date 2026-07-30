import json
import os

FILE = "contacts.json"
if os.path.exists(FILE):
    with open(FILE) as file:
        Contacts = json.load(file)
else:
    Contacts = {}
class Contact:

    def __init__(self):
        self.contact_id = ""
        self.full_name = ""
        self.phone_no = ""
        self.email = ""
        self.address = ""
    
    def create_contact(self, contact_id, full_name, phone_no, email, address):
        if contact_id in Contacts:
            print("Contact ID already exists!")
            return
        self.contact_id = contact_id
        self.full_name = full_name
        self.phone_no = phone_no
        self.email = email
        self.address = address

        Contacts[self.contact_id] = self.to_dict()

    def to_dict(self):
        return {
            "contact_id" : self.contact_id,
            "full_name" : self.full_name,
            "phone_no" : self.phone_no,
            "email" : self.email,
            "address" : self.address
        }

class ContactBook:
    def __init__(self):
        pass

    def add_contact(self):
        c = Contact()
        contact_id = input("Enter Contact ID:  ")
        full_name = input("Enter full name:  ")
        phone_no = input("Enter Phone Number:  ")
        email = input("Enter Email:  ")
        address = input("Enter Address:  ")

        c.create_contact(contact_id, full_name, phone_no, email, address)

    def save_contacts(self):
        with open(FILE, "w") as file:
            json.dump(Contacts, file, indent=4)
        print("Data saved successfully!!!")

    def update_contact(self):
        contact_id = input("Enter Contact ID:  ")
        if contact_id in Contacts:
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            print("4. Address")
            choice = input("Select field: ")
            if choice == "1":
                Contacts[contact_id]["full_name"] = input("New Name: ")
            elif choice == "2":
                Contacts[contact_id]["phone_no"] = input("New Phone: ")
            elif choice == "3":
                Contacts[contact_id]["email"] = input("New Email: ")
            elif choice == "4":
                Contacts[contact_id]["address"] = input("New Address: ")
            else:
                print("Invalid option!")
                return
            self.save_contacts()
            print("Contact Updated Successfully!")
        else:
            print("Contact not found!")

    def search_contact(self):
        contact_id = input("Enter Contact ID:  ")
        if contact_id in Contacts:
            contact = Contacts[contact_id]
            print("Contact ID:                ", contact["contact_id"])
            print("Full Name:                 ", contact["full_name"])
            print("Phone Number:              ", contact["phone_no"])
            print("Email:                     ", contact["email"])
            print("Address:                   ", contact["address"])
            print("\n------------------------------------------\n")
        else:
            print("Contact not found!!!")

    def delete_contact(self):
        contact_id = input("Enter Contact ID:  ")

        if contact_id in Contacts:

            del Contacts[contact_id]

            self.save_contacts()
            print("Contact Deleted Successfully!")
        else:
            print("Contact not found!")

    def display_all_contacts(self):
        if len(Contacts) == 0:
            print("No contacts available!")
            return

        for contact in Contacts.values():
            print("\n------------------------------")
            print("Contact ID:", contact["contact_id"])
            print("Name:", contact["full_name"])
            print("Phone:", contact["phone_no"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])

    def main_menu(self):
        while True:
            print("\n==========================================")
            print("               Contact Book               ")
            print("==========================================\n")
            print("1. Add Contact")
            print("2. Save Contacts")
            print("3. Update Contact")
            print("4. Search Contact")
            print("5. Delete Contact")
            print("6. Display All Contacts")
            print("7. Exit")
            choice = int(input("Enter choice:  "))
            if choice == 1:
                self.add_contact()
            elif choice == 2:
                self.save_contacts()
            elif choice == 3:
                self.update_contact()
            elif choice == 4:
                self.search_contact()
            elif choice == 5:
                self.delete_contact()
            elif choice == 6:
                self.display_all_contacts()
            elif choice == 7:
                print("\n==========================================")
                print("                Exiting                ")
                print("==========================================\n")
                return
            else:
                print("Invalid Choice")
                continue

def main():
    contactBook = ContactBook()
    contactBook.main_menu()

if __name__ == "__main__":
    main()