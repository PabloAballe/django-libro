from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contactame', views.contacto, name='contacto'),
]
