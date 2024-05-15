from django.urls import path
from recording_online.views import recording

urlpatterns = [
    path('recording_online/', recording),
]
