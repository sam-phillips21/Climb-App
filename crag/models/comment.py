from django.db import models

# Create your models here.
class Comment(models.Model):
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    climb_id = models.ForeignKey('Climb', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.comment} Last updated at: {self.updated_at}"