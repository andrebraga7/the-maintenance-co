from django import forms
from client_dashboard.models import Job


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['feedback']
