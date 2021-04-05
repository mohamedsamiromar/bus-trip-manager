from rest_framework import serializers
from apps.swvl_admin.models import Trip, Booking, Bus, Review, Passenger, Captin


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'bus_id', 'captin', 'from_address', 'to_address', 'from_date', 'to_date', 'price', 'reserved']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



class BookingSerializerTwo(serializers.Serializer):
    trip = serializers.IntegerField(required=True)
    reserved_seats = serializers.IntegerField(required=True)
    # serializers.EmailField(required=True)


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class CaptinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captin
        fields = '__all__'


