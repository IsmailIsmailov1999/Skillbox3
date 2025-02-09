from django import forms
from .models import Client, Campaign

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'status']

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'budget', 'clients']
