# forms.py

from django import forms
from .models import Client, Service, Campaign

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'status']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'end_date', 'budget', 'status']
