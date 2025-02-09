# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Client, Service, Campaign
from .forms import ClientForm, ServiceForm, CampaignForm

# Представление для списка клиентов
class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'client_list.html', {'clients': clients})

# Представление для создания клиента
class ClientCreateView(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'client_form.html', {'form': form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        return render(request, 'client_form.html', {'form': form})

# Представление для списка рекламных кампаний
class CampaignListView(View):
    def get(self, request):
        campaigns = Campaign.objects.all()
        return render(request, 'campaign_list.html', {'campaigns': campaigns})

# Представление для создания рекламной кампании
class CampaignCreateView(View):
    def get(self, request):
        form = CampaignForm()
        return render(request, 'campaign_form.html', {'form': form})

    def post(self, request):
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')
        return render(request, 'campaign_form.html', {'form': form})
