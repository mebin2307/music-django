from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Album, Song, Register



# class SignUpForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)    
#     class Meta:
#         model = Register
#         fields = ('name','username','password','confirm_password','email','image')

# class AlbumForm(forms.Form):

   
#     date = forms.DateField(options={"format": "YYYY-MM-DD"}, fontawesome=True)

#     class Meta:
#         model = Album
#         fields = ('artist', 'album_title', 'genre', 'album_logo','date',)

class SignUpForm(UserCreationForm):


    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # date = forms.DateField(
    #       widget=DatePicker(options={"format": "YYYY-MM-DD"}, fontawesome=True))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2', )