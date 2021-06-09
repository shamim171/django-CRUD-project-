from myapp.models import Album, Musician
from django.contrib import admin
from myapp.models import Musician, Album

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)