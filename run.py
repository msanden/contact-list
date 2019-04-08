#!/usr/bin/env python3.6
from contact import Contact

def create_contact(fname,lname,phone,email):
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    contact.save_contact()

def del_contact(contact):
    contact.delete_contact()

def find_contact(number):
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    return Contact.contact_exists(number)

def display_contacts():
    return Contact.display_contacts()

def copy_clipboard(number):
    return Contact.copy_email(number)

def main():
    print('Welcome to your contact list. Enter your name.')
    userName = input();
    print(f"What would you like to do today {userName}?")
    print('\n')

    while True:
        print("""Use this short codes to proceed: cc - create contact, dc - display contacts
        fc - find a contact ex - exit""")

        shortCode = input().lower()

        if shortCode == 'cc':
            print('New Contact')
            print('-'*10)

            print('First Name')
            fName = input();

            print('Last Name')
            lName = input();

            print('Phone Number')
            phoneNum = input();

            print('Email Address')
            emailAdd = input();

            # create and save new contact.
            save_contacts(create_contact(fName,lName,phoneNum,emailAdd))
            print('\n')
            print(f"New contact {fName} {lName} created")
            print('\n')

        elif shortCode == 'dc':
            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"""{contact.firstName} {contact.lastName}
                    {contact.phoneNumber} {contact.email}""")
                    print('\n')
            else:
                print('\n')
                print("You don't have any saved contacts.")
                print('\n')

        elif shortCode == 'fc':
            print("Enter the phone number you want to find.")
            searchNumber = input()
            if check_existing_contacts(searchNumber):
                searchContact = find_contact(searchNumber)
                print(f"Name:{searchContact.firstName} {searchContact.lastName}")
                print('-'*20)
                print(f"Phone number:{searchContact.phoneNumber}" )
                print(f"Email Address:{searchContact.email}" )
            else:
                print('Contact does not exist. Check the phone number again.')

        # Task: implement the remaining behaviors : 1. Deleting a contact. 2. Copying a contact email.

        elif shortCode == 'ex':
            print('Goodbye!')
            break

        else:
            print("I didn't understand your input. Check you shortcode.")

if __name__ == '__main__':
    main()
