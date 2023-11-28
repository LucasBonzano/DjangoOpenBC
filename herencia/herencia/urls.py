from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('herencia/', views.herencia, name='herencia'),
    path('bonzano/', views.bonzano, name='bonzano'),
    path('otravista/', views.otravista, name='otravista'),
    path('', views.index, name='index')
]
