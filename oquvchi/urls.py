from django.urls import path
from . import views
urlpatterns = [
    path('', views.oquvchi, name='maktab'),]