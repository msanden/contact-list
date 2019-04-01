import unittest;
from contact import Contact;

class TestContact(unittest.TestCase):
    """
    TestContact is a subclass (of TestCase) that defines test cases for the
    Contact class behaviors.
    TestCase is the parent class which helps create test cases.
    """

    def setUp(self):
        """ setUp() method to run before each test case."""

        self.new_contact = Contact("Manuel","Sande","3153806748","axl@glam.com");

    def tearDown(self):
        """tearDown() method that runs after each test case."""

        Contact.contactList = [];

    def test_init(self):
        """test_init() test case to test if our object is being instantiated
        correctly"""

        self.assertEqual(self.new_contact.firstName,"Manuel")
        self.assertEqual(self.new_contact.lastName,"Sande")
        self.assertEqual(self.new_contact.phoneNumber,"3153806748")
        self.assertEqual(self.new_contact.email,"axl@glam.com")

    def test_save_contact(self):
        """test_save_contact() test case to test if contact object is saved
        to contact list"""

        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contactList),1)

    def test_save_multiple_contact(self):
        """method test_save_multiple_contact() checks if we can save multiple
        contact objects to our contactList[]"""

        self.new_contact.save_contact()
        test_contact = Contact("Ednas","Nell","3806743158","axy@fab.com");
        test_contact.save_contact()
        self.assertEqual(len(Contact.contactList),2)

    def test_delete_contact(self):
        """test_delete_contact() tests if we can delete a contact from our
        contact list"""

        self.new_contact.save_contact()
        test_contact = Contact("Ednas","Nell","3806743158","axy@fab.com");
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contactList),1)

if __name__ == '__main__':
    unittest.main()
