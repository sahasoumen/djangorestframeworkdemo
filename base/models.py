from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)