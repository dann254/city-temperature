import json
import requests
import statistics
from django.conf import settings
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.locations.serializers import LocationListSerializer
from .models import City

class LocationsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = 'name'
    queryset = City.objects.all()

    def list(self, request):
        queryset = City.objects.all()
        pagination = PageNumberPagination()
        page = pagination.paginate_queryset(queryset, request)
        serializer = LocationListSerializer(page, many=True, context={'request': request})
        return pagination.get_paginated_response(serializer.data)

    def retrieve(self, request, name=None):
        if not name:
            return Response({"errors": [{"field": "name", "message": "City name cannot be empty"}]}, status=status.HTTP_400_BAD_REQUEST)

        name = name.replace('_', ' ')
        city = City.objects.get(name__iexact=name)

        if not city:
            return Response({"errors": [{"field": "name", "message": "City name not found"}]}, status=status.HTTP_404_NOT_FOUND)
        # city = get_object_or_404(queryset, name=name)
        days = self.request.query_params.get('days')
        if days:
            try:
                days = int(days)
            except TypeError:
                return Response({"errors": [{"field": "days", "message": "Number of days must be integer"}]}, status=status.HTTP_400_BAD_REQUEST)

            if days < 1 or days > 16:
                return Response({"errors": [{"field": "days", "message": "Forecasts can only be done for a maximum of 16 days and a minimum of 1 day"}]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            days = 1

        data = self.call_weather_api(city, days)
        if not data:
            return Response({"errors": [{"message": "Couldnt fetch temperature info"}]}, status=status.HTTP_400_BAD_REQUEST)
        queryset ={'temp': "100"}

        return Response(data)


    def call_weather_api(self, city, days):
        url = settings.WEATHER_URL
        key = settings.API_KEY

        params = {
            'city': city.name,
            'country': city.country,
            'days': days,
            'key':key
        }

        r = requests.get(url, params=params)

        if r.status_code == 200:
            data = r.json()
            return self.format_data(data['data'])
        else:
            return

    def format_data(self, data):
        max_temp = None
        min_temp = None
        median_temp = None
        avg_temp = None
        temps = []

        for i in data:
            temps.append(i['temp'])
            if not min_temp:
                min_temp = i['min_temp']

            if not max_temp:
                max_temp = i['max_temp']

            if i['min_temp'] < min_temp:
                min_temp = i['min_temp']

            if i['max_temp'] > max_temp:
                max_temp = i['max_temp']

        avg_temp = statistics.mean(temps)
        median_temp = statistics.median(temps)

        result = {
            'maximum': max_temp,
            'minimum': min_temp,
            'average': avg_temp,
            'median': median_temp
        }

        return result
