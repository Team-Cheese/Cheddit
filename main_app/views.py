from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Channel
from django.contrib.auth.views import LoginView

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')


def channels_index(request) :
  channels = Channel.objects.all()
  return render(request, 'channels/index.html', {'channels': channels})

def channels_detail(request , channel_id) :
  channel = Channel.objects.get(id=channel_id)
  return render(request, 'channels/detail.html', {'channel': channel})