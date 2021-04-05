from django.urls import path
from apps.captin import views

urlpatterns = [
  path('take_trip', views.take_trip, name='take_trip'),
  path('start_trip', views.start_trip, name='start_trip')
]