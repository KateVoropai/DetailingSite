from django.shortcuts import render, redirect
from .forms import AddPostForm

def recording(request):
    if request.method == 'POST':

        # user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'recording_online/recording.html')
