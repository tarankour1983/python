from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'a.html')
def profile(request):
    return HttpResponse("profile page")
