from django import forms
from .models import Category, Equipment, Job


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        }


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ['category', 'name']


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['category', 'equipment', 'description']
