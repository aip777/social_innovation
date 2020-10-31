from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import index, Index
from webcms import views
urlpatterns = [
    path('',  views.home, name='home')
]