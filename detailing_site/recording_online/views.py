from django.shortcuts import render
from django.contrib.auth.models import User

def recording(request):
    
    return render(request, 'recording_online/recording.html')
