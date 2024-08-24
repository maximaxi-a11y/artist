from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from account.utils import is_user_artist

def artist_profile(request, username):
    artist = get_object_or_404(User, username=username)
    if not is_user_artist(artist):
        return HttpResponseForbidden("Этот пользователь не является художником.")
    return render(request, 'artist_profile.html', {'artist': artist})


def index(request):
    return render(request, 'main/index.html')
