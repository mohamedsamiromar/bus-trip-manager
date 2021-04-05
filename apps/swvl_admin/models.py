from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Bus(models.Model):
    bus_number = models.CharField(null=True, max_length=50)
    color_bus = models.CharField(max_length=50, null=True)
    number_seat = models.IntegerField(null=True, default='')
    model_bus = models.TextField(max_length=100, null=True)


def __str__(self):
    return self.bus_number


class Captin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='captin')
    phone_number = models.IntegerField()
    email = models.EmailField(blank=True, null=True, max_length=254)


def __str__(self):
    return self.user.firt_name.last_name


class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='passenger')
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(blank=True, null=True, max_length=254)


def __str__(self):
    return self.user.firt_name.last_name


class Trip(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    captin = models.ForeignKey(Captin, on_delete=models.CASCADE, null=True, default='', related_name='captin_name')
    from_address = models.TextField(default='', null=True)
    to_address = models.TextField(null=True)
    from_date = models.TextField(null=True)
    to_date = models.TextField(null=True)
    price = models.IntegerField(null=False, default=0)
    reserved = models.IntegerField(null=False, default=0)


def __str__(self):
    return self.from_address


class Review(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    note = models.TextField(max_length=100)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    rate = models.CharField(null=True, max_length=10)


def __str__(self):
    return self.note


class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='bookings', null=True)
    reserved_seats = models.IntegerField(null=True)
    from_address = models.TextField(null=True)
    to_address = models.TextField(null=True)
    date_For_start_trip = models.TextField(null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    date = models.DateTimeField(default=datetime.now())


def __str__(self):
    return self.passenger