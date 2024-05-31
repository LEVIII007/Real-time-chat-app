from django.urls import path
from . import views


urlpatterns = [
    path('/room', views.room, name='room'),
    # path('room/<str:room_name>/', views.room, name='room'),
    path('<slug:slug>/', views.chat, name='chat'),
]