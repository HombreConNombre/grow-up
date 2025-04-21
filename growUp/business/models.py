from django.db import models

class Business_model(models.Model):
    business_name = models.CharField(
        unique=True,
        max_length=100
    )
    country = models.CharField(
        max_length=3
    )
