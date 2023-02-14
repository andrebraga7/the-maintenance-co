from django.contrib.auth.mixins import PermissionRequiredMixin


class ManagerAccessMixin(PermissionRequiredMixin):
    permission_required = 'manager_dashboard.manager'
