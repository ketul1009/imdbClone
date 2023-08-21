from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib import messages
from .models import *

#creating the views to show when urls are requested from the front-end

def index(request):
    movies = Movies.objects.all()
    return render(request, 'home.html', {'movies': movies})

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
            return redirect('genre')

        else:
            genre = Genre.objects.create(genre=genre)
            genre.save()
            return redirect('/')
    else:
        return render(request, 'genre.html')

def movies(request):
    if(request.method=='POST'):
        name = request.POST['name']
        genre = request.POST['genre']
        releaseDate = request.POST['releaseDate']
        if(len(name)==0 or len(genre)==0 or len(releaseDate)==0):
            messages.info(request, "Genre cannot be empty")
            return redirect('movies')

        else:
            if(Genre.objects.filter(genre=genre).exists()):
                movies = Movies.objects.create(name=name, genre=genre, releaseDate=releaseDate)
                movies.save()
                return redirect('movies')
            else:
                messages.info(request, "Genre does not exits, add genre before adding movies")
                return redirect('movies')

    else:
        movies = Movies.objects.all()
        return render(request, 'movies.html', {'movies': movies})