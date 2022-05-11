from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)


class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    contact = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    contact_type = models.CharField(max_length=20)

