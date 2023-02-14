from django.contrib.auth.mixins import PermissionRequiredMixin


class EmployeeAccessMixin(PermissionRequiredMixin):
    permission_required = 'manager_dashboard.employee'
