from django.test import TestCase
from .forms import CustomSignupForm, EditUserForm, EditProfileForm, AssignJobForm, EditJobForm


class TestCustomSignupForm(TestCase):

    def test_fields_name_and_type_are_required(self):
        form = CustomSignupForm({'name': '', 'type': ''})
        self.assertFalse(form.is_valid())

    def test_name_field_in_form(self):
        form = CustomSignupForm()
        self.assertIn('name', form.fields)

    def test_type_field_in_form(self):
        form = CustomSignupForm()
        self.assertIn('type', form.fields)


class TestEditUserForm(TestCase):

    def test_username_email_and_is_active_in_fields(self):
        form = EditUserForm()
        self.assertEqual(form.Meta.fields, ['username', 'email', 'is_active'])

    def test_username_is_required(self):
        form = EditUserForm({'username': ''})
        self.assertFalse(form.is_valid())

    def test_email_is_required(self):
        form = EditUserForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_is_active_is_required(self):
        form = EditUserForm({'is_active': ''})
        self.assertFalse(form.is_valid())


class TestEditProfileForm(TestCase):

    def test_name_is_in_fields(self):
        form = EditProfileForm()
        self.assertEqual(form.Meta.fields, ['name'])

    def test_name_is_required(self):
        form = EditProfileForm({'name': ''})
        self.assertFalse(form.is_valid())


class TestAssignJobForm(TestCase):

    def test_assignment_is_in_fields(self):
        form = AssignJobForm()
        self.assertEqual(form.Meta.fields, ['assignment'])

    def test_assignment_is_required(self):
        form = AssignJobForm({'assignment': ''})
        self.assertFalse(form.is_valid())


class TestEditJobForm(TestCase):

    def test_description_and_feedback_is_in_fields(self):
        form = EditJobForm()
        self.assertEqual(form.Meta.fields, ['description', 'feedback'])

    def test_description_is_required(self):
        form = EditJobForm({'description': ''})
        self.assertFalse(form.is_valid())

    def test_feedback_is_required(self):
        form = EditJobForm({'feedback': ''})
        self.assertFalse(form.is_valid())
