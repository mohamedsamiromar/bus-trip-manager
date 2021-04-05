from django.shortcuts import render

from apps.swvl_admin.models import Trip


def take_trip(request):
    captin = request.user.captin.get()
    trips = Trip.objects.get(captin=captin)
    return render(request, 'captin/take_trip.html', {'trips': trips})


def start_trip(request):
    if request.method == 'GET':
        trip_id = request.GET.get('trip_id')
        trip = Trip.objects.get(pk=trip_id)
        return render(request, 'captin/start_trip.html', {'trip': trip})