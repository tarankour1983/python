from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'a.html', {'titles': 'Djang o', 'link': "http://127.0.0.1:8000/"})
def profile(request):
    return render(request, 'a.html', {'titles': 'profile page', 'link': "http://youtube.com"})
