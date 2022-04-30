from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email_id=request.POST['email_id']
        password=request.POST['password']

        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email_id=email_id,password=password)
        x.save()
        print("user created")
        return redirect('/')

