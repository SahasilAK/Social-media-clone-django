from django.shortcuts import render
from django.conf import settings


DEBUG = True

def home_screen_view(request, *args, **kwargs):
    context={}
    context['debug_mode'] = settings.DEBUG
    context['room_id'] = "1"
    context['debug'] = DEBUG
    return render(request,"personal/home.html",context)
