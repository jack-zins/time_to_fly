from django.contrib import admin
from flight_scanner.models import (
    FlightAlertRequest,
    FlightAlertOrigin,
    FlightAlertDestination,
)


class FAOriginInline(admin.TabularInline):
    model = FlightAlertOrigin


class FADestinationInline(admin.TabularInline):
    model = FlightAlertDestination


@admin.register(FlightAlertRequest)
class FlightAlertRequestAdmin(admin.ModelAdmin):
    inlines = [
        FAOriginInline,
        FADestinationInline,
    ]
