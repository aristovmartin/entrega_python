from django.urls import path
from accountsApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="cuentas"),
]