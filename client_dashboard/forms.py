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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['equipment'].queryset = Equipment.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['equipment'].queryset = Equipment.objects.filter(
                    category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields[
                'equipment'
                ].queryset = self.instance.category.equipment_set.order_by(
                    'name')
