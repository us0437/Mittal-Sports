from django.contrib import admin
from django.urls import path,include
from Bookking import views as basic_views;

urlpatterns = [
    path('login',basic_views.login_user, name="login"),
    path('logout',basic_views.logout_user, name="logout"),
    path('',basic_views.home, name="home"),
    path('register',basic_views.register, name="register"),
    path('booking',basic_views.booking, name="booking"),
    path('badminton',basic_views.badminton, name="badminton"),
]