# urls.py
from django.contrib import admin
from django.urls import path, include
from .views import ClientListView, ClientCreateView, CampaignListView, CampaignCreateView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('campaigns/', CampaignListView.as_view(), name='campaign_list'),
    path('campaigns/create/', CampaignCreateView.as_view(), name='campaign_create'),
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
]
