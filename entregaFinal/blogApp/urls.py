from django.urls import path, include
from blogApp import views

urlpatterns = [
    path('', views.main, name="inicio"),
]
