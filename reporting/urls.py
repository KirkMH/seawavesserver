from django.urls import path
from . import views

urlpatterns = [
    path('track', views.route_view, name='track_boat'),
]