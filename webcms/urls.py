from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from webcms import views
urlpatterns = [
    path('',  views.home, name='home'),
    path('team/',  views.team, name='team'),
    path('about/',  views.about, name='about'),
    path('blog/',  views.blog, name='blog'),
    path('services/',  views.services, name='services'),
    path('projects/',  views.projects, name='projects'),
    path('contactus/',  views.contact_static, name='contactus'),
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    # path('blog/<int:id>', views.PostDetail.as_view(), name='post_detail'),

]