from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('signin/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path('signout/', auth_views.LogoutView.as_view(), name='logout'),
]