from django import forms
from django.forms import ModelForm
from api.models import *

class TesterForm(ModelForm):
    class Meta:
        model = TesterModel
        fields = ('name', 'email', 'phone_number',)
        labels = {
            'name': '',
            'email': '',
            'phone_number': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control p-2 mt-1', 'placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control p-2 mt-1', 'placeholder':'Email'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control p-2 mt-1', 'placeholder':'Phone number'}),
        }

class CompanyForm(ModelForm):
    class Meta:
        model = CompanyModel
        fields = ('name',)
        labels = {
            'name': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control p-2 mt-1', 'placeholder':'Name'}),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectModel
        fields = ('name', 'company',)
        labels = {
            'name': '',
            'company': 'Select company',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control p-2 mt-1', 'placeholder':'Name'}),
            'company': forms.Select(attrs={'class':'form-control p-2 mt-1'}),
        }

class HardwareForm(ModelForm):
    class Meta:
        model = HardwareModel
        fields = ('name', 'tester', 'project', 'status', 'notes',)
        labels = {
            'name': '',
            'tester': 'Select tester',
            'project': 'Select project',
            'status': 'Select status',
            'notes': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control p-2 mt-1', 'placeholder':'Name'}),
            'tester': forms.Select(attrs={'class':'form-control p-2 mt-1'}),
            'project': forms.Select(attrs={'class':'form-control p-2 mt-1'}),
            'status': forms.Select(attrs={'class':'form-control p-2 mt-1'}),
            'notes': forms.TextInput(attrs={'class':'form-control p-2 mt-1', 'placeholder':'Notes'}),
        }