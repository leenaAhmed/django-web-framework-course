from django.urls import path;

from .  import views


urlpatterns = [
    path('product/<str:name>', views.product ,  name='product'),
    path('', views.products ,  name='products'),
]
