from django.contrib import admin
from flight_scanner.models import (
    FlightAlertRequest,
    FlightAlertOrigin,
    FlightAlertDestination, 
    FlightSearchResult,
)
from flight_scanner.services.flight_alert_services import flight_itinerary_data_save


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
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        flight_itinerary_data_save(form.instance)


@admin.register(FlightSearchResult)
class FlightSearchResultsAdmin(admin.ModelAdmin):
    inlines = []
