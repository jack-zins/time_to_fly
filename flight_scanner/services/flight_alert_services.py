from django.conf import settings
from flight_scanner.models import *
import requests


def get_origin_string(far:FlightAlertRequest):
    joins = []
    for fao in far.flightalertorigin_set.all():
        joins.append(fao.airport_code)
    return ','.join(joins)


def get_destination_string(far:FlightAlertRequest):
    joins = []
    for fad in far.flightalertdestination_set.all():
        destination_type = fad.destination_type.lower()
        joins.append(f'{destination_type}:{fad.destination_name}')
    return ','.join(joins)


def get_stopover_to_string(far:FlightAlertRequest):
    minutes, seconds = divmod(far.layover_duration_limit.total_seconds(), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}:{int(minutes):02}"


def search_flights(far: FlightAlertRequest):
    params = {
        'date_from': far.start_date,
        'date_to': far.end_date,
        'max_stopover': far.layover_limit,
        'stopover_to' : get_stopover_to_string(far),
        'fly_from': get_origin_string(far),
        'fly_to' : get_destination_string(far),
        'nights_in_dst_from' : far.min_days_at_destination,
        'nights_in_dst_to' : far.max_days_at_destination,
        'adults' : far.adults,
    }
    header = {"apikey": settings.KIWI_API_KEY}
    url = 'https://tequila-api.kiwi.com/v2/search'
    responce = requests.get(url,params=params,headers=header)
    return responce.json()


def flight_itinerary_data_save(far:FlightAlertRequest):
    for result in search_flights(far)['data']:
        fsr = FlightSearchResults()
        fsr.flight_itinerary = result
        fsr.trip_id = result['id']
        fsr.flight_origin = result['flyFrom']
        fsr.flight_destination = result['flyTo']
        fsr.flight_price = result['price']
        fsr.airliner_code = result['airlines']
        fsr.save()