from atexit import register
from django.contrib import admin
from .models import User, Genre, Movies

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Movies)
