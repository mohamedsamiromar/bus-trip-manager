from django.urls import path
from apps.passenger import views


urlpatterns = [
    path('home', views.passenger_home, name='home'),
    path('where_to', views.where_to, name='where_to'),
    path('reserve', views.reserve_view, name='reserve'),
    path('review', views.review, name='review'),
    path('all_booking', views.all_booking, name='all_booking'),
]