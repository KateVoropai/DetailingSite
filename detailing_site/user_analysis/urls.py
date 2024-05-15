from django.urls import path
from user_analysis.views import analysis

urlpatterns = [
    path('user_analysis/', analysis),
]
