from django import forms
from django.contrib.auth.models import User, Permission


class UserForm(forms.Form):

    USER_TYPES = (
        ('client', 'Client'),
        ('employee', 'Employee'),
        ('manager', 'Manager'))

    name = forms.CharField(max_length=20)
    type = forms.ChoiceField(choices=USER_TYPES)

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.type = self.cleaned_data['type']
        user.save()

        if user.type == 'manager':
            permission = Permission.objects.get(codename='is_manager')
            user.user_permissions.add(permission)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        elif user.type == 'employee':
            permission = Permission.objects.get(codename='is_employee')
            user.user_permissions.add(permission)
        elif user.type == 'client':
            permission = Permission.objects.get(codename='is_client')
            user.user_permissions.add(permission)
        else:
            pass
