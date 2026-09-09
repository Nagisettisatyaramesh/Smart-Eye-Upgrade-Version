from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'company', 'phone', 'company_size', 'interest', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name', 'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Work email', 'autocomplete': 'email'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone (optional)'}),
            'interest': forms.TextInput(attrs={'placeholder': 'What are you evaluating? (optional)'}),
            'message': forms.Textarea(attrs={'placeholder': 'Anything else we should know? (optional)', 'rows': 4}),
        }
