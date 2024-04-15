import os
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from config.settings import MEDIA_URL
from musiclib.models import CustomUser

def root_for_users(request):
    lst_customuser_emails = [i.email for i in CustomUser.objects.all()]
    if not request.user.email in lst_customuser_emails:
        return HttpResponseRedirect(reverse('musiclib:login'))
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('musiclib:customuser_lst'))
    return HttpResponseRedirect(reverse('musiclib:home')) # Авторизованные несуперюзеры на страничку home

def handle_uploaded_file(f, title_trek, request):
    path = os.path.join(MEDIA_URL, f'{request.user.id}/') 
    if not os.path.isdir(path):
         os.mkdir(path) 

    if not request.user.is_authenticated:
        login_url = reverse_lazy('musiclib:login')
        return redirect(login_url)

    with open(path+title_trek+'.mp3', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)