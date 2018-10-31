# pylint: disable=E1101
from django.db import models
from django.conf import settings

from movies.models import Movie
from ratings.models import UserRating


class List(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_list = models.ManyToManyField(Movie, default=None)

    # objects = MovieListManager()

    def __str__(self):
        return f'{self.user.username} list'

    def get_user_movies(self):
        return self.movie_list.all()

    def movie_in_list(self, movie):
        return movie in self.movie_list.all()

    def add_movie_to_list(self, movie):
        new_movie = Movie.objects.get_or_create(movie)
        UserRating.objects.update_or_create_user_rating(self.user, new_movie)
        self.movie_list.add(new_movie)

    def remove_movie_from_list(self, movie):
        self.movie_list.remove(movie)
