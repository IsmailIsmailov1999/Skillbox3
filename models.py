# models.py

from django.db import models


# Статус клиента
class ClientStatus(models.TextChoices):
    POTENTIAL = 'Potential', 'Potential'
    ACTIVE = 'Active', 'Active'
    ARCHIVED = 'Archived', 'Archived'


# Модель клиента
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=ClientStatus.choices, default=ClientStatus.POTENTIAL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Модель услуги
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    clients = models.ManyToManyField(Client, related_name='services')

    def __str__(self):
        return self.name


# Статус рекламной кампании
class CampaignStatus(models.TextChoices):
    PLANNED = 'Planned', 'Planned'
    ACTIVE = 'Active', 'Active'
    COMPLETED = 'Completed', 'Completed'


# Модель рекламной кампании
class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=CampaignStatus.choices, default=CampaignStatus.PLANNED)
    clients = models.ManyToManyField(Client, related_name='campaigns')

    def __str__(self):
        return self.name

    def calculate_roi(self):
        # Пример подсчёта ROI (при условии, что у клиента есть доход)
        total_revenue = sum(client.revenue_from_campaign(self) for client in self.clients.all())
        if total_revenue == 0:
            return 0
        return (total_revenue / self.budget) * 100

