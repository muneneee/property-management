from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    agent_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Property(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    property_id = models.CharField(max_length=20)
    client_details = models.CharField(max_length=100)
    property_address = models.CharField(max_length=100)

class House(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_id = models.CharField(max_length=20)
    house_rent = models.DecimalField(max_digits=8, decimal_places=2)
    deposit = models.DecimalField(max_digits=8, decimal_places=2)

