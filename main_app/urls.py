from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('channels/', views.channels_index, name='channels_index'),
  path('channels/<str:channel_id>/', views.channels_details, name='channels_details'),
  path('channels/create/', views.ChannelCreate.as_view(), name='channels_create')
]