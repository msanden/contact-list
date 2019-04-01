import unittest;
from contact import Contact;

class TestContact(unittest.TestCase):
    """
    TestContact is a subclass (of TestCase) that defines test cases for the
    Contact class behaviors.
    TestCase is the parent class which helps create test cases.
    """

    def setUp(self):
        """ Set up method to run before each test case."""

        self.new_contact = Contact("Manuel","Sande","3153806748","axl@glam.com");

    def test_init(self):
        """test_init() test case to test if our object is being instantiated
        correctly"""

        self.assertEqual(self.new_contact.firstName,"Manuel")
        self.assertEqual(self.new_contact.lastName,"Sande")
        self.assertEqual(self.new_contact.phoneNumber,"3153806748")
        self.assertEqual(self.new_contact.email,"axl@glam.com")

if __name__ == '__main__':
    unittest.main()
