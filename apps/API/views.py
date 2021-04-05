from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.API.serializer import TripSerializer, BookingSerializer, PassengerSerializer, CaptinSerializer, \
    ReviewSerializer, BusSerializer, BookingSerializerTwo
from apps.swvl_admin.models import Trip, Booking, Review, Passenger, Bus, Captin
from rest_framework import generics, status


# @api_view(['GET', 'POST', 'PUT'])
# def tripViewApi(request):
#     if request.method == 'GET':
#         trips = Trip.objects.all()
#         serializer = Tripserializer(trips, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         tripToEdit = request.data.get('id', None)
#         trip = None
#         if tripToEdit:
#             trip = Trip.objects.get(pk=tripToEdit)
#         serializer = Tripserializer(trip, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RetrieveUpdateDestroyAPIView
class TripListApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
    lookup_field = 'id'


# class BookingListApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()
#     lookup_field = 'id'
#

class BookingView(APIView):
    def post(self, request):
        serializer = BookingSerializerTwo(data=request.data)
        if serializer.is_valid(raise_exception=True):
            trip_id = serializer.data.get('trip')
            trip = Trip.objects.get(pk=trip_id)
            reserve_seat = serializer.data.get('reserved_seats')
            if int(trip.reserved) + reserve_seat >= int(trip.bus.number_seat):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                trip.reserved += reserve_seat
                trip.save()
                booking = Booking()
                booking.trip = trip
                booking.reserved_seats = reserve_seat
                booking.passenger = request.user.passenger.get()
                booking.from_address = trip.from_address
                booking.to_address = trip.to_address
                booking.date = trip.from_date
                price = reserve_seat * trip.price
                booking.price = trip.price
                booking.total_price = price
                booking.date = datetime.now()
                booking.save()
                _serializer = BookingSerializer(booking)
                # if _serializer.is_valid():
                return Response(_serializer.data)
                # else:
                #     return Response(_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReviewListApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'



class BuslistApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Bus.objects.all()
    lookup_field = 'id'


class PassengerListApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()
    lookup_field = 'id'


class CaptinListApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CaptinSerializer
    queryset = Captin.objects.all()
    lookup_field = 'id'

# ListCreateAPIView

class TripList(generics.ListCreateAPIView):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


# class BookingList(generics.ListCreateAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()


class BusList(generics.ListCreateAPIView):
    serializer_class = BusSerializer
    queryset = Bus.objects.all()


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class PassengerList(generics.ListCreateAPIView):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()


class CaptinList(generics.ListCreateAPIView):
    serializer_class = CaptinSerializer
    queryset = Captin.objects.all()

