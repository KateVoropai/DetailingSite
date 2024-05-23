from django.urls import path
from about_us.views import index

urlpatterns = [
    path('', index, name='home')
]
