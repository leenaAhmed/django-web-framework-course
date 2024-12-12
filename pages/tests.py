from django.test import TestCase
from datetime import datetime
from .models import Contact
# Create your tests here.


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.contact = Contact.objects.create(
            full_name= "Mohamed Ahmed",
            email = 'leenaelhosary@gmail.com'
        )
    
    def test_fields(self):
        self.assertIsInstance(self.contact.full_name, str)
        self.assertIsInstance(self.contact.email, str)

    def test_timestamp(self):
        self.assertIsInstance(self.contact.created_at , datetime)

        
