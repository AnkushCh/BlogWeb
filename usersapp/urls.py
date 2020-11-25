from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usersapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersapp/logout.html'), name='logout'),

]
