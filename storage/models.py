from django.db import models

# Create your models here.

class Storage(models.Model):
    
    name = models.CharField(max_length=19, unique=True)
    owner = models.CharField(max_length=14)
