from django.contrib import admin
from django.urls import path, include
from .views import index, artist_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='main'),
    path('artist/<str:username>/', artist_profile, name='artist_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)