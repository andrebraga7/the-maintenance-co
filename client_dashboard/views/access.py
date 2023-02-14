from django.contrib.auth.mixins import PermissionRequiredMixin


class ClientAccessMixin(PermissionRequiredMixin):
    permission_required = 'manager_dashboard.client'
