from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name = "Index" ),
    path('login/', views.login, name = "login"),
    path('Registration/', views.Registration, name = "Registration"),
    path('ForgotPassword/',views.ForgotPassword, name = 'ForgotPassword'),
    path('EmailConfirmation/', views.EmailConfirmation, name = 'EmailConfirmation'),
    path('FchangePassword/', views.FchangePassword, name = 'FchangePassword'),
]