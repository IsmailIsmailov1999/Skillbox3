from django.db import models

class Client(models.Model):
    STATUS_CHOICES = [
        ('potential', 'Potential'),
        ('active', 'Active'),
        ('archived', 'Archived'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='potential')

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    clients = models.ManyToManyField(Client, related_name='services')

    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    clients = models.ManyToManyField(Client, related_name='campaigns')

    def __str__(self):
        return self.name
