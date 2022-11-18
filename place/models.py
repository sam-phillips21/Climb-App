from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.zone}. Last updated at: {self.updated_at}"