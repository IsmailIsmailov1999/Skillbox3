from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class AdvertisingCampaign(models.Model):
    name = models.CharField(max_length=255, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="campaigns")
    channel = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)


class PotentialClient(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    campaign = models.ForeignKey(AdvertisingCampaign, on_delete=models.SET_NULL, null=True, blank=True)


class Contract(models.Model):
    name = models.CharField(max_length=255, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    document = models.FileField(upload_to="contracts/")
    date_signed = models.DateField()
    duration = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)


class ActiveClient(models.Model):
    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
