from django.db import models
from django.conf import settings

from movies.models import Movie

class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=None)

    def __str__(self):
        return f'{self.movie} rating is {self.rating}'

class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, unique=True, on_delete=models.CASCADE)
    user_rating = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} rating for {self.movie} is {self.user_rating}'