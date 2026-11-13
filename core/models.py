from django.db import models

# Create your models here.
class Users(models.Model):
  username = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=25, unique=True)
  password = models.CharField(max_length=128)