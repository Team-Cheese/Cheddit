from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Channel
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def channels_index(request) :
  channels = Channel.objects.all()
  return render(request, 'channels/index.html', {'channels': channels})

def channels_details(request , channel_id) :
  channels = Channel.objects.get(id=channel_id)
  return render(request, 'channels/details.html', {'channels': channels})
