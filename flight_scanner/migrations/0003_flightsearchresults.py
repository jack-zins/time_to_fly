# Generated by Django 4.0.4 on 2022-05-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_scanner', '0002_flightalertrequest_adults_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightSearchResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=250)),
                ('flight_origin', models.CharField(max_length=4)),
                ('flight_destination', models.CharField(max_length=4)),
                ('flight_price', models.IntegerField()),
                ('airliner_code', models.CharField(max_length=15)),
                ('flight_itinerary', models.JSONField()),
            ],
        ),
    ]
