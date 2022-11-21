from django.db import models

# Create your models here.
class Climb(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.grade}. Last updated at: {self.updated_at}"