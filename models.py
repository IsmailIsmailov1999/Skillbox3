from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    """Модель предоставляемой услуги"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class AdvertisingCampaign(models.Model):
    """Модель рекламной кампании"""
    name = models.CharField(max_length=255, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="campaigns")
    channel = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class PotentialClient(models.Model):
    """Модель потенциального клиента"""
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    campaign = models.ForeignKey(AdvertisingCampaign, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    """Модель контракта"""
    name = models.CharField(max_length=255, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="contracts")
    document = models.FileField(upload_to="contracts/")
    date_signed = models.DateField()
    duration = models.IntegerField(help_text="Срок действия в днях")
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class ActiveClient(models.Model):
    """Модель активного клиента"""
    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="clients")

    def __str__(self):
        return self.potential_client.full_name
