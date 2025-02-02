from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Service, AdvertisingCampaign, PotentialClient, Contract, ActiveClient
from .serializers import (
    ServiceSerializer, AdvertisingCampaignSerializer,
    PotentialClientSerializer, ContractSerializer, ActiveClientSerializer
)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AdvertisingCampaignViewSet(viewsets.ModelViewSet):
    queryset = AdvertisingCampaign.objects.all()
    serializer_class = AdvertisingCampaignSerializer


class PotentialClientViewSet(viewsets.ModelViewSet):
    queryset = PotentialClient.objects.all()
    serializer_class = PotentialClientSerializer

    @action(detail=True, methods=['post'])
    def convert_to_active(self, request, pk=None):
        """Перевод потенциального клиента в активные"""
        potential_client = get_object_or_404(PotentialClient, pk=pk)
        contract_id = request.data.get('contract_id')
        contract = get_object_or_404(Contract, pk=contract_id)

        active_client = ActiveClient.objects.create(
            potential_client=potential_client,
            contract=contract
        )
        potential_client.delete()  # Удаляем потенциального клиента после перевода

        return Response(ActiveClientSerializer(active_client).data, status=status.HTTP_201_CREATED)


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ActiveClientViewSet(viewsets.ModelViewSet):
    queryset = ActiveClient.objects.all()
    serializer_class = ActiveClientSerializer
