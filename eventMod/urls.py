from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name='event_home'),
    path('list_events/',views.list_events, name='list_events'),
    path('add_events/',views.add_events, name='add_events'),
   
]