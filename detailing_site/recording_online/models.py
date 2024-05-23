from django.db import models

# Create your models here.

class RecordingOnline(models.Model):
    date = models.DateField()
    time = models.TimeField()
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)