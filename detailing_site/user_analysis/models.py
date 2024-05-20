from django.db import models

# Create your models here.
class UserAnalysis(models.Model):
    date = models.DateField()
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)