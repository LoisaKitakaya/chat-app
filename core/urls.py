from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.signup, name='signup'),
    path('log-in/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('log-out/', auth_views.LogoutView.as_view(), name='logout'),
    path('rooms/', views.rooms, name='rooms'),
    path('about/', views.about, name='about')
]