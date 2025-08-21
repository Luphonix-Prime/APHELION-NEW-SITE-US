from django import forms
from .models import ContactSubmission
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div

INDUSTRY_CHOICES = [
    ('', 'Select Industry'),
    ('healthcare', 'Healthcare'),
    ('financial', 'Financial Services'),
    ('government', 'Government'),
    ('education', 'Education'),
    ('technology', 'Technology'),
    ('manufacturing', 'Manufacturing'),
    ('retail', 'Retail'),
    ('energy', 'Energy & Utilities'),
    ('other', 'Other'),
]

POSITION_CHOICES = [
    ('', 'Select Position'),
    ('ciso', 'CISO'),
    ('security_analyst', 'Security Analyst'),
    ('it_manager', 'IT Manager'),
    ('compliance_manager', 'Compliance Manager'),
    ('network_admin', 'Network Administrator'),
    ('security_consultant', 'Security Consultant'),
    ('cto', 'CTO'),
    ('ceo', 'CEO'),
    ('other', 'Other'),
]

class ContactForm(forms.ModelForm):
    industry = forms.ChoiceField(choices=INDUSTRY_CHOICES, required=False)
    position = forms.ChoiceField(choices=POSITION_CHOICES, required=False)
    
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'company', 'industry', 'position', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'bg-[#0f0f0f] border border-gray-700 rounded-lg focus:ring-2 focus:ring-[#7839e9] focus:border-[#7839e9] w-full p-3 text-white',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'bg-[#0f0f0f] border border-gray-700 rounded-lg focus:ring-2 focus:ring-[#7839e9] focus:border-[#7839e9] w-full p-3 text-white',
                'placeholder': 'Work Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'bg-[#0f0f0f] border border-gray-700 rounded-lg focus:ring-2 focus:ring-[#7839e9] focus:border-[#7839e9] w-full p-3 text-white',
                'placeholder': 'Phone Number'
            }),
            'company': forms.TextInput(attrs={
                'class': 'bg-[#0f0f0f] border border-gray-700 rounded-lg focus:ring-2 focus:ring-[#7839e9] focus:border-[#7839e9] w-full p-3 text-white',
                'placeholder': 'Company'
            }),
            'industry': forms.Select(attrs={
                'class': 'bg-[#0f0f0f] border border-gray-700 rounded-lg focus:ring-2 focus:ring-[#7839e9] focus:border-[#7839e9] w-full p-3 text-white'
            }),
            'position': forms.Select(attrs={
                'class': 'bg-[#0f0f0f] border border-gray-700 rounded-lg focus:ring-2 focus:ring-[#7839e9] focus:border-[#7839e9] w-full p-3 text-white'
            }),
            'message': forms.Textarea(attrs={
                'class': 'bg-[#0f0f0f] border border-gray-700 rounded-lg focus:ring-2 focus:ring-[#7839e9] focus:border-[#7839e9] w-full p-3 text-white',
                'placeholder': 'Message',
                'rows': 4
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send Message', 
                                      css_class='w-full bg-secondary hover:bg-[#7839e9] text-white font-medium py-3 px-4 rounded-lg transition-colors'))
        self.helper.layout = Layout(
            Field('name', css_class='mb-3'),
            Field('email', css_class='mb-3'),
            Field('company', css_class='mb-3'),
            Field('message', css_class='mb-3'),
        )