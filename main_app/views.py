from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Channel, Thread
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from main_app.forms import ThreadForm
from .models import Channel, Thread, Comment
from .forms import ThreadForm, UserProfileForm, CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home( LoginView ):
  template_name = 'home.html'

def about( request ):
  return render( request, 'about.html' )

def channels_index( request ):
  channels = Channel.objects.all()
  return render( request, 'channels/index.html', { 'channels': channels })

def channels_details( request , channel_id ):
  channels = Channel.objects.get( id=channel_id )
  form = ThreadForm()
  if request.method == 'POST':
    form = ThreadForm( request.POST )
    if form.is_valid():
      form.instance.user = request.user
      new_thread = form.save( commit=False )
      new_thread.channel_id = channel_id
      new_thread.save()
  return render(request, 'channels/details.html', { 'channels': channels, 'thread_form': form, 'current_user': request.user.id })

@login_required
def thread_create( request, channel_id ):
  if request.method == 'POST':
    form = ThreadForm( request.POST )
    if form.is_valid():
      form.instance.user = request.user
      new_thread = form.save(commit=False)
      new_thread.channel_id = channel_id
      new_thread.save()
      return redirect( request, f'channels/{channel_id}' )

def threads_details( request, thread_id ):
  thread = Thread.objects.get(id=thread_id)
  comment_form = CommentForm()
  return render(request, 'thread/details.html', {'thread': thread, 'comment_form': comment_form, 'current_user': request.user.id })

@login_required
def comment_create( request, thread_id ):
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment_form.instance.user = request.user
    new_comment = comment_form.save(commit=False)
    new_comment.thread_id = thread_id
    new_comment.save()
  return redirect(f'/thread/{thread_id}', thread_id=thread_id)

class ChannelCreate( LoginRequiredMixin, CreateView ):
  model = Channel
  fields = '__all__'
  success_url = '/channels/'

class Home( LoginView ):
  template_name = 'home.html'
  
class ChannelUpdate( LoginRequiredMixin, UpdateView ):
  model = Channel
  fields = '__all__'
  
class ChannelDelete( LoginRequiredMixin, DeleteView ):
  model = Channel
  success_url = '/channels/'
  
class ThreadDelete( LoginRequiredMixin, DeleteView ):
  model = Thread
  success_url = '/channels/'
  
class ThreadUpdate( LoginRequiredMixin, UpdateView ):
  model = Thread
  fields = '__all__'
  success_url = '/channels/'

class CommentDelete( LoginRequiredMixin, DeleteView ):
  model = Comment 
  success_url = '/thread/{thread_id}/'
  

def signup( request ):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm( request.POST )
    if form.is_valid():
      user = form.save()
      login( request, user )
      return redirect('profile')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render( request, 'signup.html', context )

def profile( request ):
  error_message = ''
  if request.method == 'POST':
    form = UserProfileForm( request.POST )
    if form.is_valid():
      form.instance.user = request.user
      form.save()
      return redirect('http://localhost:8000/channels')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserProfileForm()
  context = { 'form': form, 'error_message': error_message }
  return render( request, 'profile.html', context )


