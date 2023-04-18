from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    client_details = models.CharField(max_length=100)
    property_address = models.CharField(max_length=100)

class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    house_rent = models.DecimalField(max_digits=8, decimal_places=2)
    deposit = models.DecimalField(max_digits=8, decimal_places=2)

class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    rent = models.DecimalField(max_digits=8, decimal_places=2)
    garbage_service = models.DecimalField(max_digits=8, decimal_places=2)

class Receipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)