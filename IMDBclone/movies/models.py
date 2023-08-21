from django.db import models

class User(models.Model):
    username = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Genre(models.Model):
    genre = models.CharField(max_length=15)

class Movies(models.Model):
    user = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length=100)

