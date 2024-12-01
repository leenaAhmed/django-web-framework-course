from django.urls import path;

from .  import views


urlpatterns = [
    path('prduct', views.product ,  name='prduct'),
    path('', views.products ,  name='products'),
]
