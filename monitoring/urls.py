from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('boats/', views.boat_listview, name='boat_list'),
    path('map/', views.map_view, name='map'),
    path('boats/dt', views.BoatDTListView.as_view(), name='boat_dtlist'),
    path('boats/<int:pk>/view', views.record_listview, name='record_list'),
    path('boats/<int:pk>/view/dt', views.RecordDTListView.as_view(), name='record_dtlist'),
    path('instructions/', views.instructions_view, name='instructions_page'),
]
