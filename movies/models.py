# pylint: disable=E1101
from django.db import models
from django.urls import reverse
from django.db.models import signals

from movieSiteDjango.utils import get_unique_slug


class MovieManager(models.Manager):
    def get_or_create(self, movie):
        qs = self.get_queryset().filter(title=movie.title)
        if qs.count() == 1:
            print('old movie')
            new_movie = qs.first()
            return new_movie
        print('new movie', movie)
        movie.save()
        return movie


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    poster = models.CharField(max_length=500)
    year = models.IntegerField()

    objects = MovieManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    def get_movie_rating(self):
        return self.rating.rating

    def get_user_rating(self, user):
        user_rating_qs = self.userrating_set.filter(user=user)
        if user_rating_qs.count() == 1:
            user_rating_obj = user_rating_qs.first()
            return user_rating_obj.user_rating
        return None


def movie_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug(instance, instance.title)


signals.pre_save.connect(movie_pre_save_reciever, sender=Movie)
