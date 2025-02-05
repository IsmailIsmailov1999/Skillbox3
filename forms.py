from django import forms
from .models import Service, Campaign, PotentialClient, Contract, ActiveClient

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'

class PotentialClientForm(forms.ModelForm):
    class Meta:
        model = PotentialClient
        fields = '__all__'

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

class ActiveClientForm(forms.ModelForm):
    class Meta:
        model = ActiveClient
        fields = '__all__'
