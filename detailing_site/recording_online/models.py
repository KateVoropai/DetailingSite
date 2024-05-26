from django.db import models

# Create your models here.

class RecordingOnline(models.Model):
    date = models.DateField(verbose_name="дата")
    time = models.TimeField(verbose_name="время")
    car_number = models.CharField(max_length=30, verbose_name="номер автомобиля")
    fullname = models.CharField(max_length=50, verbose_name="имя")
    phone_number = models.CharField(max_length=30, verbose_name="номер телефона")