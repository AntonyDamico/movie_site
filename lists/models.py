# pylint: disable=E1101
from django.db import models
from django.conf import settings

from movies.models import Movie

class List(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_list = models.ManyToManyField(Movie, default=None)

    # objects = MovieListManager()

    def __str__(self):
        return f'{self.user.username} list'

    def get_user_movies(self):
        return self.movie_list.all()