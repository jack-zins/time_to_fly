# Generated by Django 4.0.4 on 2022-05-14 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightAlertRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('layover_limit', models.IntegerField()),
                ('layover_duration_limit', models.DurationField()),
                ('min_days_at_destination', models.IntegerField(default=0)),
                ('max_days_at_destination', models.IntegerField(default=0)),
                ('adults', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FlightSearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=250)),
                ('flight_origin', models.CharField(max_length=4)),
                ('flight_destination', models.CharField(max_length=4)),
                ('airliner_code', models.CharField(max_length=15)),
                ('flight_itinerary', models.JSONField()),
                ('flight_alert_requests', models.ManyToManyField(to='flight_scanner.flightalertrequest')),
            ],
        ),
        migrations.CreateModel(
            name='FlightSearchResultPriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('flight_search_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scanner.flightsearchresult')),
            ],
        ),
        migrations.CreateModel(
            name='FlightAlertOrigin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_code', models.CharField(max_length=3)),
                ('flight_alert_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scanner.flightalertrequest')),
            ],
        ),
        migrations.CreateModel(
            name='FlightAlertDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_type', models.CharField(choices=[('Airport', 'Airport'), ('City', 'City'), ('State', 'State'), ('Country', 'Country')], max_length=10)),
                ('destination_name', models.CharField(max_length=250)),
                ('flight_alert_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scanner.flightalertrequest')),
            ],
        ),
    ]
