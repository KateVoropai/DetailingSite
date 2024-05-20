from django.db import models

# Create your models here.


class Category(models.Model):
    name_category = models.CharField(max_length=30, unique=True)
class Price(models.Model):
    name_service = models.CharField(max_length=30, unique=True)
    car = models.PositiveIntegerField()
    jeep = models.PositiveIntegerField()
    minivan = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Portfolio(models.Model):
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/')    


