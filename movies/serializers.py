# pylint: disable=E1101
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'slug', 'poster', 'year')

class UserMovieSerializer(serializers.ModelSerializer):
    user_rating = serializers.IntegerField()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'slug', 'poster', 'year', 'user_rating')