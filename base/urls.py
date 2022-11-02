from django.urls import path, include
from .views import CustomLoginView, profile, settings, users,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('users/', users, name='users'),
    path('profile/', profile, name='profile'),
    path('settings/', settings, name='settings'),
    path('register/', RegisterPage, name='register'),
]