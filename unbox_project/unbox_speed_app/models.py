from django.db import models
from django.utils import timezone

# Create your models here.
class SpeedData(models.Model):
    speed = models.FloatField(max_length=255)  
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Speed Data"

    def __str__(self):
        return f"{self.speed} + {self.timestamp}"
     
   
