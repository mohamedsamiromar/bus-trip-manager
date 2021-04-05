from django import forms

from apps.swvl_admin.models import Trip, Bus


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['bus', 'captin', 'from_address', 'to_address', 'from_date', 'to_date', 'price']


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['number_seat', 'bus_number', 'color_bus', 'model_bus']