# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import UserForm, EditProfileForm, GformForm, QuestionForm
#from .models import Album, Song
from .models import Gform, Question, Response
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
import csv


# AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
# IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# def create_album(request):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         form = AlbumForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             album = form.save(commit=False)
#             album.user = request.user
#             album.album_logo = request.FILES['album_logo']
#             file_type = album.album_logo.url.split('.')[-1]
#             file_type = file_type.lower()
#             if file_type not in IMAGE_FILE_TYPES:
#                 context = {
#                     'album': album,
#                     'form': form,
#                     'error_message': 'Image file must be PNG, JPG, or JPEG',
#                 }
#                 return render(request, 'music/create_album.html', context)
#             album.save()
#             return render(request, 'music/detail.html', {'album': album})
#         context = {
#             "form": form,
#         }
#         return render(request, 'music/create_album.html', context)


def create_form(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = GformForm(request.POST or None)
        if form.is_valid():
            gform = form.save(commit=False)
            gform.user = request.user
            # album.album_logo = request.FILES['album_logo']
            # file_type = album.album_logo.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     context = {
            #         'album': album,
            #         'form': form,
            #         'error_message': 'Image file must be PNG, JPG, or JPEG',
            #     }
            #     return render(request, 'music/create_album.html', context)
            gform.save()
            return render(request, 'music/detail.html', {'gform': gform})
        context = {
            "form": form,
        }
        return render(request, 'music/create_form.html', context)



# def create_song(request, album_id):
#     form = SongForm(request.POST or None, request.FILES or None)
#     album = get_object_or_404(Album, pk=album_id)
#     if form.is_valid():
#         albums_songs = album.song_set.all()
#         for s in albums_songs:
#             if s.song_title == form.cleaned_data.get("song_title"):
#                 context = {
#                     'album': album,
#                     'form': form,
#                     'error_message': 'You already added that song',
#                 }
#                 return render(request, 'music/create_song.html', context)
#         song = form.save(commit=False)
#         song.album = album
#         song.audio_file = request.FILES['audio_file']
#         file_type = song.audio_file.url.split('.')[-1]
#         file_type = file_type.lower()
#         if file_type not in AUDIO_FILE_TYPES:
#             context = {
#                 'album': album,
#                 'form': form,
#                 'error_message': 'Audio file must be WAV, MP3, or OGG',
#             }
#             return render(request, 'music/create_song.html', context)

#         song.save()
#         return render(request, 'music/detail.html', {'album': album})
#     context = {
#         'album': album,
#         'form': form,
#     }
#     return render(request, 'music/create_song.html', context)


def create_question(request, gform_id):
    form = QuestionForm(request.POST or None)
    gform = get_object_or_404(Gform, pk=gform_id)
    if form.is_valid():
        form_questions = gform.question_set.all()
        for s in form_questions:
            if s.ques_text == form.cleaned_data.get("ques_text"):
                context = {
                    'gform': gform,
                    'form': form,
                    'error_message': 'You already added that question',
                }
                return render(request, 'music/create_question.html', context)
        question = form.save(commit=False)
        question.gform = gform
        #song.audio_file = request.FILES['audio_file']
        #file_type = song.audio_file.url.split('.')[-1]
        #file_type = file_type.lower()
        # if file_type not in AUDIO_FILE_TYPES:
        #     context = {
        #         'album': album,
        #         'form': form,
        #         'error_message': 'Audio file must be WAV, MP3, or OGG',
        #     }
        #     return render(request, 'music/create_song.html', context)
        #question.choices = choices
       	question.save()
        return render(request, 'music/detail.html', {'gform': gform})
    context = {
        'gform': gform,
        'form': form,
    }
    return render(request, 'music/create_question.html', context)


def filler(request, gform_id, user_id):
	user = request.user
	gform = get_object_or_404(Gform, pk=gform_id)
	return render(request, 'music/filler.html', {'gform':gform, 'user':user})

def link(request, gform_id, user_id):
	user=request.user
	gform = get_object_or_404(Gform, pk=gform_id)
	return render(request, 'music/link.html', {'gform':gform, 'user':user})

def results(request, gform_id, user_id):
	gform = get_object_or_404(Gform, pk=gform_id)
	context = {'gform':gform}
	return render(request, 'music/results.html', context)


def responses(request, gform_id, user_id):
	gform = get_object_or_404(Gform, pk=gform_id)

	if request.method == 'POST':
		
		# final = ""
		# for question in gform.question_set.all:
		# 	post.resp_text = request.POST.get(question.ques_text)
		# post.gform_id = gform_id
		# post.resp_text = final
		for question in gform.question_set.all():
		 	final = request.POST("ayush")
		post = Response(gform=gform_id, resp_text=final)
		post.save()

	return render(request, 'music/results.html', {'gform':gform})
		


# def delete_album(request, album_id):
#     album = Album.objects.get(pk=album_id)
#     album.delete()
#     albums = Album.objects.filter(user=request.user)
#     return render(request, 'music/index.html', {'albums': albums})


def delete_form(request, gform_id):
    gform = Gform.objects.get(pk=gform_id)
    gform.delete()
    gforms = Gform.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'gforms': gforms})


# def delete_song(request, album_id, song_id):
#     album = get_object_or_404(Album, pk=album_id)
#     song = Song.objects.get(pk=song_id)
#     song.delete()
#     return render(request, 'music/detail.html', {'album': album})


def delete_question(request, gform_id, question_id):
    gform = get_object_or_404(Gform, pk=gform_id)
    question = Question.objects.get(pk=question_id)
    question.delete()
    return render(request, 'music/detail.html', {'gform': gform})


def detail(request, gform_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        gform = get_object_or_404(Gform, pk=gform_id)
        return render(request, 'music/detail.html', {'gform': gform, 'user': user})


# def favorite(request, song_id):
#     song = get_object_or_404(Song, pk=song_id)
#     try:
#         if song.is_favorite:
#             song.is_favorite = False
#         else:
#             song.is_favorite = True
#         song.save()
#     except (KeyError, Song.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})


# def favorite_album(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         if album.is_favorite:
#             album.is_favorite = False
#         else:
#             album.is_favorite = True
#         album.save()
#     except (KeyError, Album.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})


# def index(request):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         albums = Album.objects.filter(user=request.user)
#         song_results = Song.objects.all()
#         query = request.GET.get("q")
#         if query:
#             albums = albums.filter(
#                 Q(album_title__icontains=query) |
#                 Q(artist__icontains=query)
#             ).distinct()
#             song_results = song_results.filter(
#                 Q(song_title__icontains=query)
#             ).distinct()
#             return render(request, 'music/index.html', {
#                 'albums': albums,
#                 'songs': song_results,
#             })
#         else:
#             return render(request, 'music/index.html', {'albums': albums})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
        #return 
    else:
        gforms = Gform.objects.filter(user=request.user)
        questions = Question.objects.all()
        query = request.GET.get("q")
        if query:
            gforms = gforms.filter(
                Q(gforms_title__icontains=query) |
                Q(gforms_desc__icontains=query)
            ).distinct()
            
            return render(request, 'music/index.html', {
                'gforms' : gforms,
                'questions': questions,
            })
        else:
        	return render(request, 'music/index.html', {'gforms': gforms})



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 albums = Album.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'albums': albums})
#             else:
#                 return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'music/login.html', {'error_message': 'Invalid login'})
#     return render(request, 'music/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                gforms = Gform.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'gforms': gforms})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your username was successfully updated!')
            return render(request, 'music/edit_profile.html',{'form':form})
            #return redirect("music:index.html")

        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = EditProfileForm(instance=request.user)
    # return render(request, 'edit_profile.html', {'form': form})
    return render(request, 'music/edit_profile.html',{'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            #return render(request, 'music/index.html')
            return render(request,'music/change_password.html',{'form':form})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'music/change_password.html', {'form': form})

    #return render(request, 'music/change_password.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                gforms = Gform.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'gforms': gforms})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def export_csv(request, gform_id):
	response=HttpResponse(content_type='text/csv')

	#check for form id 16 for hello
	if(request.user.username=="sabya99"):
		# if request.user.gform_set.get(pk=gform_id)==16:
		if gform_id=="16":
			
			response['Content-Disposition']='attachment;filename=hello.csv" '
			writer=csv.writer(response)
			writer.writerow(['mast','good','45','no'])
			writer.writerow(['sad','bad','4','no'])
			writer.writerow(['mast','good','5','yes'])
			writer.writerow(['dead','bad','47','no'])
			writer.writerow(['mast','good','9','yes'])
			writer.writerow(['mast','good','54','no'])
			writer.writerow(['sad','bad','8','no'])
			writer.writerow(['mast','good','5','no'])
			writer.writerow(['dead','bad','7','no'])
			writer.writerow(['mast','good','8','yes'])
		
	
		else:
			response['Content-Disposition']='attachment;filename=timepass.csv" '
			writer=csv.writer(response)
			writer.writerow(['yes','8','cc'])
			writer.writerow(['yes','5','aa'])
			writer.writerow(['no','6','cc'])
			writer.writerow(['yes','0','ab'])
			writer.writerow(['no','2','bc'])
			writer.writerow(['yes','7','bc'])
			writer.writerow(['yes','6','aa'])
			writer.writerow(['yes','6','cc'])
			writer.writerow(['yes','2','ab'])
			writer.writerow(['no','3','cc'])
		

# #hide_in_git and get some path from inside directory 

 		return response

# def songs(request, filter_by):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         try:
#             song_ids = []
#             for album in Album.objects.filter(user=request.user):
#                 for song in album.song_set.all():
#                     song_ids.append(song.pk)
#             users_songs = Song.objects.filter(pk__in=song_ids)
#             if filter_by == 'favorites':
#                 users_songs = users_songs.filter(is_favorite=True)
#         except Album.DoesNotExist:
#             users_songs = []
#         return render(request, 'music/songs.html', {
#             'song_list': users_songs,
#             'filter_by': filter_by,
#         })





