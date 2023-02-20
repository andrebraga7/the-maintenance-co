from django.test import TestCase
from .forms import CustomSignupForm


class TestCustomSignupForm(TestCase):

    def test_fields_name_and_type_are_required(self):
        form = CustomSignupForm({'name': '', 'type': ''})
        self.assertFalse(form.is_valid())
