# pylint: disable=E1101
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    movie_rating = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'slug', 'poster', 'year', 'movie_rating')


class UserMovieSerializer(serializers.ModelSerializer):
    movie_rating = serializers.IntegerField()
    user_rating = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'slug', 'poster',
                  'year', 'movie_rating', 'user_rating')
