from rest_framework import serializers

from .models import Climb

class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Climb