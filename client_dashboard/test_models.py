from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Equipment
from manager_dashboard.models import Profile


class TestModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(
            username='testuser',
            email='email@email.com',
            profile=Profile(name='Test Name')
            )

        cls.category = Category.objects.create(
            name='Test Category', user=cls.test_user)

        cls.equipment = Equipment.objects.create(
            name='Test Equipment', category=cls.category, user=cls.test_user)

    def test_type_default_to_3(self):
        self.assertEqual(self.test_user.profile.type, 3)

    def test_category_has_foreign_user(self):
        self.assertEqual(self.category.user.username, 'testuser')

    def test_equipment_has_correct_category(self):
        self.assertEqual(self.equipment.category.name, 'Test Category')
