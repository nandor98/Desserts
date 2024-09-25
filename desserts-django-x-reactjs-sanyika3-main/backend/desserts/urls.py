from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('desserts/', views.GetAll,name="GetAll"),
    path('', views.indexPage, name="index")
]