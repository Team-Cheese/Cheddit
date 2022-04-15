from django.urls import path
from . import views

urlpatterns = [
  path( '', views.Home.as_view(), name='home' ),
  path( 'about/', views.about, name='about' ),
  path( 'channels/', views.channels_index, name='channels_index' ),
  path( 'channels/create/', views.ChannelCreate.as_view(), name='channels_create' ),
  path( 'channels/<str:channel_id>/create_thread/', views.thread_create, name='thread_create' ),
  path( 'channels/<str:channel_id>/', views.channels_details, name='channels_details' ),
  path( 'thread/<str:thread_id>/', views.threads_details, name='threads_details' ),
  path( 'thread/<str:thread_id>/create_comment/', views.comment_create, name='comment_create' ),
  path( 'channels/<str:pk>/update>/', views.ChannelUpdate.as_view(), name='channels_update' ),
  path( 'channels/<str:pk>/delete>/', views.ChannelDelete.as_view(), name='channels_delete' ),
  path( 'thread/<str:pk>/delete>/', views.ThreadDelete.as_view(), name='threads_delete' ),
  path( 'thread/<str:pk>/update>/', views.ThreadUpdate.as_view(), name='threads_update' ),
  path( 'thread/<str:pk>/comment_delete', views.CommentDelete.as_view(), name='comment_delete' ),
  path( 'accounts/signup', views.signup, name='signup' ),
  path( 'accounts/profile', views.profile, name='profile' )
]
