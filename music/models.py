from __future__ import unicode_literals

from django.db import models
import os.path
from django import forms
from django.core.urlresolvers import reverse

# Create your models here.


class Album(models.Model):

    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to='static/images/')


    def get_absolute_url(self):
        print("adada", self.id)
        return reverse('music:detail', kwargs={'pk': self.id})

    
    def __str__(self):
        print("adada", self.id)
        return "%s" % (self.album_title)

class Register(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=500)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/profile/')

   
class Song(models.Model):
    model = Album
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='static/upload/audio', help_text=("Allowed type - .mp3, .wav, .ogg"))
    song_title = models.CharField(max_length=150)

    

    class Meta:
        ordering = ('song_title',)

    def get_absolute_url(self):
        print("adada", self.id)
        return reverse('music:play', kwargs={'pk': self.id})

    def __str__(self):
        return "%s" % (self.song_title)
