from rest_framework import serializers
from .models import Cinema, Movie, Screening


class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.HyperlinkedIdentityField(view_name='cinema-detail')
    movies = serializers.SlugRelatedField(many=True, slug_field='title', queryset=Movie.objects.all())
    class Meta:
        model = Cinema
        fields = ('name', 'city', 'movies')


class ScreeningSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())

    class Meta:
        model = Screening
        fields = ("movie", "cinema", "date")
