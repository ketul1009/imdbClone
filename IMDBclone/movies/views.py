from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib import messages
from .models import *

#creating the views to show when urls are requested from the front-end

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def register(request):
    if(request.method=='POST'):
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']

        if( User.objects.filter(email=email).exists()):
            messages.info(request, "Email already used")
            return redirect('register')

        elif( User.objects.filter(username=username).exists()):
            messages.info(request, "Username not available")
            return redirect('register')
        
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'registem.html')

def login(request):
    if(request.method=='POST'):
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if(user is not None):
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

def genre(request):
    if(request.method=='POST'):
        genre = request.POST['genre']

        if(len(genre) == 0):
            messages.info(request, "Genre cannot be empty")

        else:
            user = User.objects.create_user(genre=genre)
            user.save()
            return redirect('/')
    else:
        return render(request, 'genre.html')
