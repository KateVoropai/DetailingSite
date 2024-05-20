from django.db import models

# Create your models here.

class RecordingOnline(models.Model):
    date = models.DateField()
    time = models.TimeField()
