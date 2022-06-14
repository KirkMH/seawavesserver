from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('boat/', views.boat_listview, name='boat_list'),
    path('boat/dt', views.BoatDTListView.as_view(), name='boat_dtlist'),
]
