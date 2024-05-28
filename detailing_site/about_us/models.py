from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=30, unique=True, verbose_name="наименование категории")

    def __str__(self) -> str:
        return self.name_category


class Price(models.Model):
    name_service = models.CharField(max_length=30, unique=True, verbose_name="наименование сервиса")
    car = models.PositiveIntegerField(verbose_name="легковой автомобиль")
    jeep = models.PositiveIntegerField(verbose_name="джип")
    minivan = models.PositiveIntegerField(verbose_name="минивэн")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', verbose_name="категория")
    describe_service = models.CharField(max_length=500, default='Описание', verbose_name="описание сервиса")

    def __str__(self) -> str:
        return self.name_service


class Portfolio(models.Model):
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name="фото")    

