from django.db import models
from django.urls import reverse
from django.db.models import signals

from movieSiteDjango.utils import get_unique_slug

class MovieManager(models.Manager):
    def get_or_create(self, movie):
        # change the movie dict to a qs
        # check if the new qs is in the Movie.objects.all()
            # return the movie
        # create a new movie and return it
        print('movie exists!!!!', movie in Movie.objects.all())
        return ''

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

def movie_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug(instance, instance.title)

signals.pre_save.connect(movie_pre_save_reciever, sender=Movie)