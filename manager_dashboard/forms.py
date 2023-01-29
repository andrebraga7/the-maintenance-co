from django import forms
from django.contrib.auth.models import User


class CustomSignupForm(forms.Form):

    USER_TYPES = (
        ('client', 'Client'),
        ('employee', 'Employee'),
        ('manager', 'Manager'))

    name = forms.CharField(max_length=20)
    type = forms.ChoiceField(choices=USER_TYPES)

    def signup(self, request, user):
        up = user.profile
        up.name = self.cleaned_data['name']
        up.type = self.cleaned_data['type']
        up.save()
