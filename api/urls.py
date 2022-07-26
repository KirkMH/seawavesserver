from django.urls import path
from . import views

urlpatterns = [
    path('boats', views.BoatListView.as_view()),
    path('locations', views.BoatLocationsListView.as_view()),
    path('boat/add', views.addBoat),
    path('settings', views.getSettings),
    path('', views.getRecords),
    path('record/add', views.addRecord),
    path('boat/<int:pk>/route', views.getBoatRoute),
]
