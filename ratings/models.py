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


class UserRatingManager(models.Manager):
    def rate_movie(self, user, movie, user_rating):
        self.update_or_create_rating(user, movie, user_rating)
        rating_obj = movie.rating
        rating_obj.rating = (rating_obj.rating + user_rating)/2
        rating_obj.save()

    def update_or_create_rating(self, user, movie, user_rating):
        qs = self.get_queryset().filter(user=user, movie=movie)
        print('qs!!!! ', qs)
        if qs.count() == 1:
            old_rating = qs.first()
            old_rating.rating = user_rating
            old_rating.save()
        else:
            new_user_rating = UserRating(user=user, movie=movie, user_rating=user_rating)
            new_user_rating.save()

    # def remove_old_rating(self, old_rating, new_rating):
    #     rating_obj = movie.rating
        # rating_obj.rating = 

class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True, null=True, on_delete=models.CASCADE)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    user_rating = models.PositiveIntegerField(default=0)

    objects = UserRatingManager()

    def __str__(self):
        return f'{self.user} rating for {self.movie} is {self.user_rating}'
