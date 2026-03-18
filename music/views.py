# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from .models import Album, Song, Register
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from music.forms import SignUpForm


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_Album_list'
    print('hii')

    def get_queryset(self):
        print("queryset")
        """Return the last five published questions."""
        return Album.objects.all()

class AlbumCreate(CreateView):
    models = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'album_form.html'
    print("album create")
    print(fields[3:4])


    def get_queryset(self):
        """Return the last five published questions."""
        return Album.objects.all()

# class UserCreate(CreateView):
#     forms = SignUpForm()
#     models = Register
#     fields = ['name','username','password','email','image']
#     template_name = 'registration/singup.html'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Register.objects.all()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('music:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/singup.html', {'form': form})

class AlbumUpdate(UpdateView):
    models = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'album_form.html'
    print("album create")

    def get_queryset(self):
        """Return the last five published questions."""
        return Album.objects.all()

class SongAdd(CreateView):
    models = Song
    fields = ['album', 'audio_file', 'song_title']
    template_name = 'song_form.html'
    print("song add")

    def get_queryset(self):
        """Return the last five published questions."""
        return Song.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'detail.html'

class PlayView(generic.DetailView):
    """docstring for ClassName"""
    model = Song
    template_name = 'play.html'
    print("jnvdnvldn create")    

    def get_queryset(self):
        print("queryset")
        """Return the last five published questions."""
        return Song.objects.all()
    

class SongView(generic.ListView):
    model = Song
    template_name = 'song.html'
    context_object_name = 'latest_Song_list'

    print('hii')

    def get_queryset(self):
        print("queryset")
        """Return the last five published questions."""
        return Song.objects.all()

    

def search(request):
        album_list = Album.objects.all()
        quuery = request.GET.get("q")
        print('search')
        if quuery:
            album_list = album_list.filter(artist__icontains=quuery)

        context = {'latest_Album_list': album_list}
        return render(request, 'index.html', context)
