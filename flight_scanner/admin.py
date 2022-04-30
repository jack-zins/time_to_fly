from django.contrib import admin
from flight_scanner.models import FlightAlertRequest,FlightAlertOrigin,FlightAlertDestination
# Register your models here.



class FAOInLine(admin.TabularInline):
    model = FlightAlertOrigin

class FADinLine(admin.TabularInline):
    model = FlightAlertDestination

@admin.register(FlightAlertRequest)
class FlightAlertRequestAdmin(admin.ModelAdmin):
    inlines = [FADinLine,FAOInLine]

