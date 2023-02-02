from django import forms
from django.contrib.auth.models import User
from .models import Profile


USER_TYPES = ((3, 'Client'), (2, 'Employee'), (1, 'Manager'))


class CustomSignupForm(forms.Form):
    name = forms.CharField(max_length=20)
    type = forms.ChoiceField(choices=USER_TYPES)

    def signup(self, request, user):
        up = user.profile
        up.name = self.cleaned_data['name']
        up.type = self.cleaned_data['type']
        up.save()


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': None,
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name']
