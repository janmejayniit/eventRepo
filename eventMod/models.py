from django.db import models

# Create your models here.
class Events(models.Model):
    event_name = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    