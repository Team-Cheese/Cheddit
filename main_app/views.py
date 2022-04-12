from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Channel
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from main_app.forms import ThreadForm
from .models import Channel, Thread
from .forms import ThreadForm, UserProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
  form = ThreadForm(request.POST)
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST, instance=request.user)
    profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      userprofile = profile_form.save()
      login(request, user)
      return redirect('')
    else:
      error_message = 'Invalid sign up - try again'
  user_form = UserCreationForm()
  userprofile_form = UserProfileForm()
  context = {'user_form': user_form, 'userprofile_form': userprofile_form, 'error_message': error_message}
  return render(request, 'signup.html', context)

