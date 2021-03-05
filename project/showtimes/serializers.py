from rest_framework import serializers
from .models import Cinema

class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = ('url', 'name', 'city', 'movies')