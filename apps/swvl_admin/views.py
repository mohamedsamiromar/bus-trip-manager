from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from apps.swvl_admin.form import TripForm, BusForm
from apps.swvl_admin.models import Trip, Bus, Captin, Booking


# def create_trip(request):
#     if request.method == 'GET':
#         buses = Bus.objects.all()
#         captins = Captin.objects.all()
#         return render(request, 'create_trip.html', {'captins': captins, 'buses': buses})
#     elif request.method == 'POST':
#
#         from_address = request.POST.get('from_address')
#         to_address = request.POST.get('to_address')
#         from_date = request.POST.get('from_date')
#         to_date = request.POST.get('to_date')
#
#         bus_id = request.POST.get('bus')
#         captin_id = request.POST.get('captin')
#
#         bus = Bus.objects.get(pk=bus_id)
#         captin = Captin.objects.get(pk=captin_id)
#
#         trip = Trip()
#         trip.bus = bus
#         trip.captin = captin
#         trip.from_address = from_address
#         trip.to_address = to_address
#         trip.from_date = from_date
#         trip.to_date = to_date
#         trip.save()
#         return render(request, 'list_trip.html')



def admin_page(request):
    return render(request, 'swvl_admin/admin_page.html')


def list_trip(request):
    trips = Trip.objects.all()
    paginator = Paginator(trips, 20)
    page_number = request.GET.get('pages')
    pages = paginator.get_page(page_number)
    return render(request, 'swvl_admin/list_trip.html', {'trips': pages, 'pages': pages})


def create_trip(request):
    buses = Bus.objects.all()
    captins = Captin.objects.all()
    trip = None
    trip_form = None

    if request.method == 'GET':
        if 'trip_id' in request.GET:
            trip_id = request.GET.get("trip_id")
            trip = Trip.objects.get(pk=trip_id)
        else:
            trip = Trip()

    elif request.method == 'POST':

        if 'id' in request.POST and request.POST.get('id') is not '':
            id = request.POST.get('id')
            trip = Trip.objects.get(pk=id)
            trip_form = TripForm(request.POST, instance=trip)
            if trip_form.is_valid():
                trip = trip_form.save()
        else:
            trip_form = TripForm(request.POST)
            if trip_form.is_valid():
                trip = trip_form.save()
    return render(request, 'swvl_admin/create_trip.html', {'captins': captins, 'buses': buses, 'trip': trip, 'form': trip_form})


def busView(request):
    bus = None
    busform = None
    if request.method == 'GET':
        if 'bus_id' in request.GET:
            bus_id = request.GET.get("bus_id")
            bus = Bus.objects.get(pk=bus_id)
        else:
            bus = Bus()
    elif request.method == 'POST':
        if 'id' in request.POST and request.POST.get('id') is not '':
            id = request.POST.get('id')
            bus = Bus.objects.get(pk=id)
            busform = BusForm(request.POST, instance=bus)
            if busform.is_valid():
                bus = busform.save()
        else:
            busform = BusForm(request.POST)
            if busform.is_valid():
                bus = busform.save()
    return render(request, 'swvl_admin/create_bus.html', {'bus': bus, 'form': busform})


def list_captin(request):
    captins = Captin.objects.all()
    return render(request, 'swvl_admin/list_captin.html', {'captins': captins})


def remove_captin(request):
    if request.method == 'GET':
        captin_id = request.GET.get('captin_id')
        Captin.objects.get(pk=captin_id).delete()
        return list_captin(request)


def list_bus(request):
    buses = Bus.objects.all()
    return render(request, 'swvl_admin/remove_bus.html', {'buses': buses})


def delete_bus(request):
    if request.method == "GET":
        bus_id = request.GET.get('bus_id')
        Bus.objects.get(pk=bus_id).delete()
        return list_bus(request)



# def list_booking(request):
#     booking = Booking.objects.all()
#     paginator = Paginator(booking, 20)
#     page_number = request.GET.get('pages')
#     pages = paginator.get_page(page_number)
#     return render(request, 'swvl_admin/list_booking.html', {'booking': pages, 'pages': pages})


def get_all_booking(request):
    booking = Booking.objects.all()
    return render(request, 'swvl_admin/all_booking.html', {'booking': booking})