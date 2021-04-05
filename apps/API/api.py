from apps.swvl_admin.models import Trip, Booking, Bus, Review
from apps.API.serializer import Tripserializer, Bookingserializer, Busserializer, Reviewserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def trip_list_api(request):
    all_trip = Trip.objects.all()
    data = Tripserializer(all_trip, many=True).data
    return Response({'data': data})


@api_view(['GET', 'POST'])
def booking_list_api(request):
    all_booking = Booking.objects.all()
    data = Bookingserializer(all_booking, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def bus_list_api(request):
    all_bus = Bus.objects.all()
    data = Busserializer(all_bus, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def review_list_api(request):
    all_review = Review.objects.all()
    data = Reviewserializer(all_review, many=True).data
    return Response({'data': data})
