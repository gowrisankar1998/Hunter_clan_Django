from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('guidelines',views.guidelines,name='guidelines'),
    path('events',views.events,name='events'),
    path('scoreboard',views.scoreboard,name='scoreboard'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path('notification',views.notification,name='notification'),
    path('login',auth_views.LoginView.as_view(template_name='hunter_game/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='hunter_game/home.html'),name='logout'),
    path('profile',views.profile,name='profile'),
]
