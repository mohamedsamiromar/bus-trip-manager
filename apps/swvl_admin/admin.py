from django.contrib import admin

# Register your models here.
from apps.swvl_admin.models import Trip, Bus, Booking, Review, Captin, Passenger

admin.site.register(Trip)
admin.site.register(Bus)
admin.site.register(Booking)
admin.site.register(Captin)
admin.site.register(Passenger)
admin.site.register(Review)
