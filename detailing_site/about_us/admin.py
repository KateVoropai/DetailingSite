from django.contrib import admin
from .models import Category, Price, Portfolio

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_service', 'car', 'jeep', 'minivan', 'category')
    list_display_links = ('id', 'name_service', 'car', 'jeep', 'minivan', 'category')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')

