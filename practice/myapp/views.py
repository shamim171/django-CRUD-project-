from os import name
import re
from myapp.models import Musician, Album
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from myapp import forms

# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'musician_list':musician_list} 
    return render(request, 'myapp/index.html', context=diction)

def album_list(request,artist_id):
    musician_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist_id = artist_id)
    diction ={'musician_info':musician_info,'album_list':album_list}
    return render(request, 'myapp/album_list.html', context=diction)

def add_album(request):
    form = forms.AlbumForm()
    
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
    diction = {'form':form}
    return render(request, 'myapp/add_album.html', context=diction)

def edit_album(request,album_id):
    albums = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=albums)
    diction = {}
    
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=albums)
        
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated!!!'})
        
    diction.update({'albums':albums,'form':form})
    diction.update({'album_id':album_id})
    return render(request, 'myapp/edit_album.html', context=diction)

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_message':'Album Deleted Successfully!!!'}
    return render(request, 'myapp/delete.html', context=diction)


def add_musician(request):
    musician_form = forms.MusicianForm()
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save(commit=True)
            return index(request)
        
    diction = {'musician_form':musician_form}
    return render(request, 'myapp/add_musician.html', context=diction)

def edit_musician(request,artist_id):
    musicians = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=musicians)
    diction ={}
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musicians)
        
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated!!!'})
            return index(request)
        
    diction.update({'musicians':musicians, 'form':form})
    return render(request, 'myapp/edit_musician.html', context=diction)

def delete_musician(request,artist_id):
    musician = Musician.objects.get(pk=artist_id).delete()
    
    diction = {'delete_message':'Musician Deleted Successfully!!!'}
    return render(request, 'myapp/delete.html', context=diction)


