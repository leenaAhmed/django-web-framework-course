from django.urls import path;

from .  import views

# app_name='pagesapp' 
urlpatterns = [
    path('', views.index ,  name='index'),
    path('about', views.about ,  name='about'),
    path('contact', views.contactform ,  name='contact'),
]
