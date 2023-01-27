from django import forms


class CustomSignupForm(forms.Form):

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
