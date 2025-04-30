from django import forms
from .models import Works



class WorkForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['title']
        labels = {
            'title' : ''
        }
        # widgets = {
        #     'title':forms.TextInput(attrs={'class': 'form-input'}) , 
        #     'is_complited': forms.CheckboxInput(attrs={'class': 'form-checkbox'})
        # }
        