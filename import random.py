import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found!")
        return
    print("\nContact List:")
    print("-" * 40)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print("-" * 40)

# Search contact by name or phone
def search_contact():
    query = input("Enter Name or Phone Number to Search: ").strip().lower()
    contacts = load_contacts()
    
    found_contacts = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    
    if found_contacts:
        print("\nSearch Results:")
        print("-" * 40)
        for contact in found_contacts:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            print("-" * 40)
    else:
        print("No matching contact found.")

# Update an existing contact
def update_contact():
    name = input("Enter the Name of the Contact to Update: ").strip()
    contacts = load_contacts()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Leave blank if you don’t want to update a field.")
            new_phone = input("Enter New Phone Number: ").strip() or contact["phone"]
            new_email = input("Enter New Email: ").strip() or contact["email"]
            new_address = input("Enter New Address: ").strip() or contact["address"]

            contact["phone"], contact["email"], contact["address"] = new_phone, new_email, new_address
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact():
    name = input("Enter the Name of the Contact to Delete: ").strip()
    contacts = load_contacts()
    
    filtered_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    
    if len(filtered_contacts) == len(contacts):
        print("Contact not found.")
    else:
        save_contacts(filtered_contacts)
        print("Contact deleted successfully!")

# User-friendly menu
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
