from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    text = models.TextField(default='DEFAULT VALUE')