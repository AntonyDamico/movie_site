from django.db import models
from django.conf import settings

from movies.models import Movie


class RatingManager(models.Manager):
    def add_rating_to_movie(self, movie, rating=0):
        new_movie_rating = Rating(movie=movie, rating=rating)
        new_movie_rating.save()


class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)

    objects = RatingManager()

    def __str__(self):
        return f'{self.movie} rating is {self.rating}'


class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, unique=True, on_delete=models.CASCADE)
    user_rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user} rating for {self.movie} is {self.user_rating}'
