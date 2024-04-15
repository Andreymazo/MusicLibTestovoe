import os
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from config.settings import BASE_DIR, BASE_URL, MEDIA_ROOT, MEDIA_URL
from musiclib.forms import MyAuthForm
from musiclib.func_for_help import handle_uploaded_file, root_for_users
from musiclib.models import CustomUser
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import MusicFilesFilterForm, MusicFilesForm, SignupForm
from .models import CustomUser, MusicFiles
from pydub import AudioSegment 

def signup_without_confirmation(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.email_value = form.cleaned_data['email'] 
           user.password1_value = form.cleaned_data['password1']
           user.password2_value = form.cleaned_data['password2']
           custom_user_value = CustomUser.objects.create(email=user.email_value)
           custom_user_value.set_password(user.password2_value)
           custom_user_value.save()
           return HttpResponseRedirect(reverse('musiclib:login'))
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = MyAuthForm
    model = CustomUser

def home(request):
        root_for_users(request) 
        request_user_email=request.user.email
        request_user_id = request.user.id
        customuser_queryset = MusicFiles.objects.all().filter(customuser=request_user_id)
        file_filter_form=MusicFilesFilterForm(request.POST)
        context = {
            'request_user_email':request_user_email,
            'customuser_queryset':customuser_queryset,
            'request_user_id': request_user_id,
            'file_filter_form':file_filter_form
        }
        if file_filter_form.is_valid():
                    
                    min_id_value = file_filter_form.cleaned_data['min_id']
                    max_id_value = file_filter_form.cleaned_data['max_id']
                    title_value = file_filter_form.cleaned_data['title_for_search']
                    
                    if file_filter_form.cleaned_data['min_id']:
                        customuser_queryset=customuser_queryset.filter(id__gte=min_id_value)
                    if file_filter_form.cleaned_data['max_id']:
                        customuser_queryset=customuser_queryset.filter(id__lte=max_id_value)
                    if file_filter_form.cleaned_data['title_for_search']:
                        customuser_queryset=customuser_queryset.filter(title=title_value)
                    if file_filter_form.cleaned_data['title_for_search'] and file_filter_form.cleaned_data['max_id'] and file_filter_form.cleaned_data['min_id']:
                        customuser_queryset=customuser_queryset.filter(id__gte=min_id_value).filter(id__lte=max_id_value).filter(title=title_value)
                    if file_filter_form.cleaned_data['title_for_search'] and file_filter_form.cleaned_data['max_id'] :
                        customuser_queryset=customuser_queryset.filter(id__lte=max_id_value).filter(title=title_value)
                    if file_filter_form.cleaned_data['title_for_search'] and file_filter_form.cleaned_data['min_id']:
                        customuser_queryset=customuser_queryset.filter(id__gte=min_id_value).filter(title=title_value)
                        
                        
                    context = {
                            'request_user_email':request_user_email,
                            'customuser_queryset':customuser_queryset,
                            'request_user_id': request.user.id,
                            'file_filter_form':file_filter_form
                        }
            
            
        return render(request, 'musiclib/templates/home.html', context)

def upload(request):

    if request.method == 'POST':
        form = MusicFilesForm(request.POST,request.FILES)
        if form.is_valid():
             title=request.POST['title']
             file = handle_uploaded_file(request.FILES['file'], title, request) 
             instance = MusicFiles.objects.create(title=title, file=file, customuser=request.user)
             instance.save()
             return HttpResponseRedirect(reverse('musiclib:home'))
    else:
        form = MusicFilesForm()
    context = {'form':form,}
    return render(request, 'upload.html', context)

def cutter_file(request, pk1, pk2): # Номер трека из библиотеки пользователя, Id пользователя
    request_user_id=pk2
    customuser_queryset = MusicFiles.objects.all().filter(customuser=request_user_id)
    song = customuser_queryset.get(id=pk1)
    song_in = f'{BASE_DIR}/media/{request_user_id}/{song.title}.mp3'
    song_for_cut = AudioSegment.from_mp3(song_in) 
    ten_seconds = 10 * 1000
    first_10_seconds = song_for_cut[:ten_seconds] 
    # # last_5_seconds = song[-5000:] 
    first_10_seconds.export(f"media/{request_user_id}/new{pk1}{song.title}.mp3", format="mp3") 
    return HttpResponseRedirect(reverse('musiclib:home'))

