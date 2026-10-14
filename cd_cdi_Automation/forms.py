from django import forms

from cd_cdi_Automation.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'position']
        labels = {'name': 'Full name', 'email': 'Email address', 'position': 'Position'}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Aarav Sharma', 'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@company.com', 'autocomplete': 'email'}),
            'position': forms.TextInput(attrs={'placeholder': 'e.g. Product Designer', 'autocomplete': 'organization-title'}),
        }
