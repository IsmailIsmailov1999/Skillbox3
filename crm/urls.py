from django.urls import path
from .views import client_list, client_create, campaign_list, campaign_create

urlpatterns = [
    path('clients/', client_list, name='client_list'),
    path('clients/create/', client_create, name='client_create'),
    path('campaigns/', campaign_list, name='campaign_list'),
    path('campaigns/create/', campaign_create, name='campaign_create'),
]
