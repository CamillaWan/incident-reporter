from django.urls import path
from . import views

urlpatterns = [
    path('', views.incident_list, name='incident_list'),
    path('add/', views.add_incident, name='add_incident'),
    path('load-more/', views.load_more_incidents, name='load_more_incidents'),
]