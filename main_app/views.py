from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Channel
from django.contrib.auth.views import LoginView


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


def channels_index(request) :
  channels = Channel.objects.all()
  return render(request, 'channels/index.html', {'channels': channels})

def channels_details(request , channel_id) :
  channels = Channel.objects.get(id=channel_id)
  return render(request, 'channels/details.html', {'channel': channels})

class ChannelCreate(CreateView):
  model = Channel
  fields = '__all__'
  success_url = '/channels/'

class Home(LoginView):
  template_name = 'home.html'

class ChannelUpdate(UpdateView) :
  model = Channel
  fields = '__all__'

class ChannelDelete(DeleteView) :
  model = Channel
  success_url = '/channels/'