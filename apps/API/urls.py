from django.urls import path
from apps.API import views
urlpatterns = [
    # RetrieveUpdateDestroyAPIView
    path('api_trip/<int:id>', views.TripListApi.as_view(), name='api_trip'),
    # path('api_booking/<int:id>', views.BookingListApi.as_view(), name='api_booking'),
    path('api_bus/<int:id>', views.BuslistApi.as_view(), name='api_bus'),
    path('api_review/<int:id>', views.ReviewListApi.as_view(), name='api_review'),
    path('api_passenger/<int:id>', views.PassengerListApi.as_view(), name='api_passenger'),
    path('api_captin/<int:id>', views.CaptinListApi.as_view(), name='api_captin'),

    #List & create
    path('api_list_trip', views.TripList.as_view(), name='trip'),
    path('api_list_bus', views.BusList.as_view(), name='bus'),
    # path('api_list_booking', views.BookingList.as_view(), name='booking'),
    path('api_list_passenger', views.PassengerList.as_view(), name='passenger'),
    path('api_list_captin', views.CaptinList.as_view(), name='captin'),
    path('api_list_review', views.ReviewList.as_view(), name='review'),


    #custom
    path('booking', views.BookingView.as_view(), name='booking')
]



