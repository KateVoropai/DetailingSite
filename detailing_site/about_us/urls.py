from django.urls import path
from about_us.views import index, price

urlpatterns = [
    path('', index, name='home'),
    path('price/', price, name='price_list'),
]
