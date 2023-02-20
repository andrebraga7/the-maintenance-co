from django.test import TestCase
from .views import ManagerAccessMixin
from client_dashboard.models import Job, Category, Equipment


class TestAccessMixin(TestCase):

    def test_access_mixin_is_manager_permission(self):
        permission = ManagerAccessMixin()
        self.assertEqual(permission.permission_required, 'manager_dashboard.manager')


class TestViews(TestCase):

    def test_new_jobs_view(self):
        response = self.client.get('/accounts/login/?next=/manager/new_jobs')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_active_jobs_view(self):
        response = self.client.get('/accounts/login/?next=/manager/active_jobs')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_completed_jobs_view(self):
        response = self.client.get('/accounts/login/?next=/manager/completed_jobs')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
