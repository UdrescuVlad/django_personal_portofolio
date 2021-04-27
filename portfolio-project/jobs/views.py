from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'jobs/home.html')

def vlad(request):
    return render(request, 'jobs/vlad.html')