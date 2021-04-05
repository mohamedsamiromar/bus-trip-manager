from django import forms

from apps.swvl_admin.models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['passenger', 'reserved_seats', 'from_address', 'to_address', 'date_For_start_trip', 'trip', 'price',
                  'total_price', 'date']