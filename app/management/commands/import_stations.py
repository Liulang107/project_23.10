import csv

from django.core.management.base import BaseCommand
from app.models import Station, Route


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', newline='', encoding='cp1251') as csvfile:

            stations_reader = csv.DictReader(csvfile, delimiter=';')

            for row in stations_reader:
                station = Station()
                station.name = row['Name']
                station.longitude = row['Longitude_WGS84']
                station.latitude = row['Latitude_WGS84']
                station.save()

                routes = [route for route in row['RouteNumbers'].split('; ')]
                for route in routes:
                    object = Route.objects.filter(name=route).first()
                    if object:
                        station.routes.add(object)
                    else:
                        route = Route(name=route)
                        route.save()
                        station.routes.add(route)
                station.save()