from django.db import models
from django.contrib.auth.models import User



class Pokemon(models.Model):
    name = models.CharField(max_length=255, null=True)
    types = models.CharField(max_length=255, null=True)
    text = models.TextField(default='',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pokemon", null=True)

    def __str__(self) -> str:
        return self.name