from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import Profile
from client_dashboard.models import Job


USER_TYPES = ((3, 'Client'), (2, 'Employee'), (1, 'Manager'))


class CustomSignupForm(forms.Form):
    name = forms.CharField(max_length=20)
    type = forms.ChoiceField(choices=USER_TYPES)

    def signup(self, request, user):
        up = user.profile
        up.name = self.cleaned_data['name']
        up.type = self.cleaned_data['type']
        up.save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            FloatingField(
                'username',
                'email',
                'name',
                'type',
                'password1',
                'password2',
            )
        )


class EditUserForm(forms.ModelForm):

    is_active = forms.ChoiceField(
        choices=[(True, 'Active'), (False, 'Inactive')])

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            FloatingField('username', 'email', 'is_active')
        )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            FloatingField('name')
        )


class AssignJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['assignment']

    assignment = forms.ModelChoiceField(User.objects.filter(profile__type='2'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            FloatingField('assignment')
        )


class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['description', 'feedback']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            FloatingField('description', 'feedback')
        )
