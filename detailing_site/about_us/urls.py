from django.urls import path
from about_us.views import about_company

urlpatterns = [
    path('company/', about_company)
]