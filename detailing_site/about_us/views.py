from django.shortcuts import render

def about_company(request):
    return render(request, 'about_us/index.html')
