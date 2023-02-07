from django import forms
from .models import Category


class AddCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        }
