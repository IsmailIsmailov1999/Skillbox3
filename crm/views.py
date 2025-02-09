from django.shortcuts import render, redirect
from .models import Client, Service, Campaign
from .forms import ClientForm, CampaignForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'crm/client_form.html', {'form': form})

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'crm/campaign_list.html', {'campaigns': campaigns})

def campaign_create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'crm/campaign_form.html', {'form': form})
