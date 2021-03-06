from django.db import models



class FlightAlertRequest(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    layover_limit = models.IntegerField()
    layover_duration_limit = models.DurationField()
    min_days_at_destination = models.IntegerField(default=0)
    max_days_at_destination = models.IntegerField(default=0)
    adults = models.IntegerField(default=1)


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


class FlightSearchResult(models.Model):
    flight_alert_requests = models.ManyToManyField('FlightAlertRequest')
    trip_id = models.CharField(max_length=250)
    flight_origin = models.CharField(max_length=4)
    flight_destination = models.CharField(max_length=4)
    airliner_code = models.CharField(max_length=15)
    flight_itinerary = models.JSONField()


class FlightSearchResultPriceHistory(models.Model):
    flight_search_result = models.ForeignKey('FlightSearchResult', on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField()
