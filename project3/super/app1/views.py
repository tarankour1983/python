from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'a.html',{'titles':'Django','link':'http://youtube.com'})
def profile(request):
    return render(request, 'a.html',{'titles':'Profile page','link':'http://127.0.0.1:8000/'})
def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request,'output.html',{'result':c})
