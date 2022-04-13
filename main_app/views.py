from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Channel
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from main_app.forms import ThreadForm
from .models import Channel, Thread
from .forms import ThreadForm, UserProfileForm, CommentForm
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

def threads_details(request, thread_id):
  thread = Thread.objects.get(id=thread_id)
  comment_form = CommentForm()
  print(thread.title)
  return render(request, 'thread/details.html', {'thread': thread, 'comment_form': comment_form})

def comment_create(request, thread_id):
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    new_comment = comment_form.save(commit=False)
    new_comment.thread_id = thread_id
    new_comment.save()
  return redirect('/channels/', thread_id=thread_id)


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
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('profile')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def profile(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserProfileForm(request.POST)
    if form.is_valid():
      form.instance.user = request.user
      print(form)
      print(request.user)
      # This will add the user to the database
      form.save()
      # This is how we log a user in
      return redirect('http://localhost:8000/channels')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserProfileForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'profile.html', context)


