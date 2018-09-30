# pylint: disable=E1101
from django.db import models
from django.conf import settings

from movies.models import Movie

class MovieList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_list = models.ManyToManyField(Movie, default=None)

    def __str__(self):
        return f'{self.user.username} profile'
