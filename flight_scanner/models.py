from django.db import models


# Create your models here.
class FlightAlertRequest(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    layover_limit = models.IntegerField()
    layover_duration_limit = models.DurationField()


class FlightAlertOrigin(models.Model):
    flight_alert_request = models.ForeignKey('FlightAlertRequest', on_delete=models.CASCADE)
    airport_code = models.CharField(max_length=3)


class FlightAlertDestination(models.Model):
    DST_AIRPORT = 'Airport'
    DST_CITY = 'City'
    DST_STATE = 'State'
    DST_COUNTRY = 'Country'
    DST_CHOICES = [
        (DST_AIRPORT, 'Airport'),
        (DST_CITY, 'City'),
        (DST_STATE, 'State'),
        (DST_COUNTRY, 'Country'),
    ]
    flight_alert_request = models.ForeignKey('FlightAlertRequest', on_delete=models.CASCADE)
    destination_type = models.CharField(choices=DST_CHOICES, max_length=10)
    destination_name = models.CharField(max_length=250)
