from builtins import int
from datetime import datetime

from django.shortcuts import render

# Create your views here.
from apps.passenger.form import BookingForm
from apps.swvl_admin.models import Trip, Booking, Review


def passenger_home(request):
    return render(request, 'passenger/passenger_home.html')


def all_booking(request):
    passenger = request.user.passenger.get()
    bookings = Booking.objects.filter(passenger=passenger)
    return render(request, 'passenger/all_booking.html', {'bookings': bookings})


def where_to(request):
    from_address = request.POST.get('from_address')
    to_address = request.POST.get('to_address')
    date = request.POST.get('date')
    reserved = request.POST.get('reserved_seat')

    if date is None or from_address is None or from_address is None:
        return render(request, 'passenger/where_to.html')
    else:
        trips = Trip.objects.filter(from_date__lte=date, to_date__gte=date, from_address=from_address,
                                    to_address=to_address)

    return render(request, 'passenger/where_to.html',
                  {'trips': trips, 'from_address': from_address, 'to_address': to_address,
                   "from_date": date, 'reserved': reserved})


def reserve_view(request):
    if request.method == "GET":
        trip_id = request.GET.get('trip_id')
        trip = Trip.objects.get(pk=trip_id)

        return render(request, 'passenger/reserve.html', {'trip': trip})
    elif request.method == "POST":
        reserve_seat = int(request.POST.get('reserve_seats'))
        trip_id = request.POST.get('trip_id')
        trip = Trip.objects.get(pk=trip_id)
        if int(trip.reserved) + reserve_seat >= int(trip.bus.number_seat):
            return render(request, 'passenger/bus_page_error.html',
                          {'errors': 'BUS IS FULL CAN YOU CHOICE ANOTHER BUS'})
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
    return render(request, 'passenger/where_to.html')


def review(request):
    if request.method == "GET":
        trip_id = request.GET.get('trip_id')
        trip = Trip.objects.get(pk=trip_id)
        return render(request, 'passenger/review.html', {'trip': trip})
    elif request.method == "POST":
        trip = int(request.POST.get('trip_id'))
        review = Review()
        review.trip = Trip.objects.get(pk=trip)
        review.note = request.POST.get('note')
        review.rate = request.POST.get('rate')
        review.passenger = request.user.passenger.get()
        review.save()
    return render(request, 'passenger/passenger_home.html')