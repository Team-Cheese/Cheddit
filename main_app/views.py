from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Channel
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect

from main_app.forms import ThreadForm
from .models import Channel, Thread
from .forms import ThreadForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def channels_index(request) :
  channels = Channel.objects.all()
  return render(request, 'channels/index.html', {'channels': channels})

def channels_details(request , channel_id) :
  channels = Channel.objects.get(id=channel_id)

  thread_form = ThreadForm()
  return render(request, 'channels/details.html', {'channels': channels, 'thread_form': thread_form})

def thread_create(request, channel_id):
  form = ThreadForm(request.POST, request.FILES)
  if form.is_valid():
    new_thread = form.save(commit=False)
    new_thread.channel_id = channel_id
    new_thread.save()
  return redirect('/channels/', channel_id=channel_id)

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
