from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Gform, Question


# class AlbumForm(forms.ModelForm):

#     class Meta:
#         model = Album
#         fields = ['artist', 'album_title', 'genre', 'album_logo']


class GformForm(forms.ModelForm):

    class Meta:
        model = Gform
        fields = ['gform_name', 'gform_desc']


# class SongForm(forms.ModelForm):

#     class Meta:
#         model = Song
#         fields = ['song_title', 'audio_file']

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['ques_type', 'ques_text','choices', 'is_req', 'is_vis']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class EditProfileForm(UserChangeForm):
    password=None

    class Meta:
        model=User
        fields = ('username',)





