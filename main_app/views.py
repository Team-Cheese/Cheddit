from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Channel
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Channel(CreateView) :
  model = Channel
  fields = '__all__'


def channel_index(request) :
  channels = Channel.objects.all()
  return render(request, 'channel/index.html', {'channel': channels})