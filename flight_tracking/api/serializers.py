from rest_framework import serializers
from .models import Airport, Flight

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['code', 'city']


class FlightSerializer(serializers.ModelSerializer):
    from_airport_ = serializers.ReadOnlyField()
    to_ = serializers.ReadOnlyField()
    class Meta:
        model = Flight
        fields = ['flight_number', 'take_off','landing','from_airport_','to_']