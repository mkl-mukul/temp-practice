from django.db import models

# Create your models here.

class Tasks(models.Model):
    task=models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id}:{self.task}"