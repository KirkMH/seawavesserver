from django.urls import path
from . import views

urlpatterns = [
    path('boats', views.getBoats),
    path('boat/add', views.addBoat),
    path('settings', views.getSettings),
    path('', views.getRecords),
    path('record/add', views.addRecord),
]
