from django.urls import path
from apps.swvl_admin import views

urlpatterns = [
    path('admin_page', views.admin_page, name='admin_page'),
    path('list_trip', views.list_trip, name='list_trip'),
    path('create_trip', views.create_trip, name='create_trip'),
    path('add_bus', views.busView, name='add_bus'),
    path('list_captin', views.list_captin, name='list_captin'),
    path('buses', views.list_bus, name='buses'),
    path('delete_bus', views.delete_bus, name='delete_bus'),
    # path('list_booking', views.list_booking, name='list_booking'),
    path('remove_captin', views.remove_captin, name='remove_captin'),
    path('booking_all', views.get_all_booking, name='booking_all'),

]