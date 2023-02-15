from django import forms
from .models import Category, Equipment, Job


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ""


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


class EditJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['description']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
