from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_event, name='create_event'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
    path('register/<int:id>/', views.register_event, name='register_event'),
]