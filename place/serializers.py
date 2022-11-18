from rest_framework import serializers

from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Location