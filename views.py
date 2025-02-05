from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Campaign, PotentialClient, Contract, ActiveClient
from .forms import ServiceForm, CampaignForm, PotentialClientForm, ContractForm, ActiveClientForm
from django.db.models import Count, Sum
from django.shortcuts import render

def campaign_statistics(request):
    stats = Campaign.objects.annotate(
        total_clients=Count('potentialclient'),
        converted_clients=Count('potentialclient__activeclient'),
        total_revenue=Sum('potentialclient__activeclient__contract__amount')
    ).values('name', 'total_clients', 'converted_clients', 'total_revenue')

    return render(request, 'statistics/campaign_stats.html', {'stats': stats})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_form.html', {'form': form})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})
