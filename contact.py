class Contact:
    """
    class that creates new instances of a contact
    """
    contactList = [];

    def __init__(self,firstName,lastName,phoneNumber,email):
        self.firstName = firstName;
        self.lastName = lastName;
        self.phoneNumber = phoneNumber;
        self.email = email;

    def save_contact(self):
        """
        save_contact() method saves contacts to contactList
        """
        Contact.contactList.append(self);

    def delete_contact(self):
        Contact.contactList.remove(self);
