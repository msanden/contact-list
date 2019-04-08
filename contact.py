import pyperclip;

class Contact:
    """
    class that creates new instances of a contact.
    """
    contactList = [];

    def __init__(self,firstName,lastName,phoneNumber,email):
        self.firstName = firstName;
        self.lastName = lastName;
        self.phoneNumber = phoneNumber;
        self.email = email;

    def save_contact(self):
        """
        save_contact() method saves contacts to contactList.
        """
        Contact.contactList.append(self);

    def delete_contact(self):
        Contact.contactList.remove(self);

    @classmethod
    def find_by_number(cls,number):
        """
        Method that takes in a number and returns the contact that matches that number.
        number: is the phone-number to search for.
        """
        for contact in cls.contactList:
            if contact.phoneNumber == number:
                return contact

    @classmethod
    def contact_exists(cls,number):
        for contact in cls.contactList:
            if contact.phoneNumber == number:
                return True

        return False

    @classmethod
    def display_contacts(cls):
        return cls.contactList

    @classmethod
    def copy_email(cls,number):
        contactFound = Contact.find_by_number(number)
        pyperclip.copy(contactFound.email)
