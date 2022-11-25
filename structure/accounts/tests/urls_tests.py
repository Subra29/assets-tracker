'''
This file contains 
    - URL testing '
'''

from django.test import SimpleTestCase
from django.urls import (
    resolve,
)
from structure.accounts.views import (
    RegisterAPIView,
    APILoginView
)

class AccountsTestURL(SimpleTestCase):

    def test_Register_URL (self):
        resolver = resolve('/register/')
        self.assertEqual(resolver.func.__name__,RegisterAPIView.as_view().__name__)

    def test_Login_URL (self):
        resolver = resolve('/api/token/')
        self.assertEqual(resolver.func.__name__,APILoginView.as_view().__name__)