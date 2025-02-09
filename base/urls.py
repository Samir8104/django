from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="leHome"),
    path('room/', views.room, name="leRoom")
]