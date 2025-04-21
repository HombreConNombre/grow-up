from django.db import models

class Users(models.Model):
    user_name = models.CharField(
        max_length=40,
        blank=False
    )
    first_name = models.CharField(
        blank=True
    )
    last_name = models.CharField(
        blank=True
    )
    bio = models.CharField(
        max_length=100,
        blank=True
        )
    location = models.CharField(
        max_length=150, 
        blank=True
        )
