from django.contrib import admin
from tapsi_app.models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'driver', 'customer', 'trip_cost', 'payment_status')
    search_fields = ('driver__first_name', 'customer__first_name', 'trip_id')
