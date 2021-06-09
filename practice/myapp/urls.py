from os import name
from re import VERBOSE
from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_musician/', views.add_musician, name='add_musician'),
    path('edit_musician/<int:artist_id>/', views.edit_musician, name='edit_musician'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_musician/<int:artist_id>/', views.delete_musician, name='delete_musician')
]