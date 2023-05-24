from django.urls import path
from . import views

urlpatterns = [
    path('boats', views.BoatListView.as_view()),
    path('locations', views.BoatLocationsListView.as_view()),
    path('boat/add', views.addBoat),
    path('settings', views.getSettings),
    path('boat/detail', views.getBoatDetail),
    path('boat/local', views.saveBoatLocalData),
    path('', views.getRecords),
    path('record/add', views.addRecord),
    path('boat/route', views.getBoatRoute),
    path('voyage/start', views.startVoyage),
    path('voyage/stop', views.stopVoyage),
]
