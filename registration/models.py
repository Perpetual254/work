from django.db import models


class workers(models.Model):
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)
      phone_number = models.CharField(blank=True, max_length=100)
      age = models.IntegerField(blank=True, null=True)
      email = models.EmailField(unique=True)
      field= models.CharField(max_length=100)

# Create your models here.
