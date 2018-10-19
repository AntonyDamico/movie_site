# pylint: disable=E1101
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from movies.models import Movie


class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.movie} rating is {self.rating}'


def add_rating_to_movie_post_reciever(sender, instance, created, *args, **kwargs):
    if instance and created:
        Rating.objects.get_or_create(movie=instance)


post_save.connect(add_rating_to_movie_post_reciever, sender=Movie)


class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, unique=True, on_delete=models.CASCADE)
    user_rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user} rating for {self.movie} is {self.user_rating}'
