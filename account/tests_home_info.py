from django.test import TestCase
from hospital.account.views import Contact, home, aboutus, Signup

class TestContact(TestCase):
    @classmethod
    def setupTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass
def setUp(self):
    print("setUp: Run once for every test method to setup clean data.")
    pass
def test_contact_1(self):
    print("Method: test_contact_1")
    self.assertTemplateUsed('account/contact.html')
def test_home_1(self):
    print("Method: test_contact_1")
    self.assertTemplateUsed('account/home.html')
def test_aboutus_1(self):
    print("Method: test_contact_1")
    self.assertTemplateUsed('account/aboutus.html')
def test_signup_1(self):
    print("Method: test_contact_1")
    self.assertTemplateUsed('account/signup.html')
