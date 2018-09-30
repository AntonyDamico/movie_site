from django.db import models
from django.urls import reverse
from django.db.models import signals

from movieSiteDjango.utils import get_unique_slug

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    poster = models.CharField(max_length=500)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

def movie_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug(instance, instance.title)

signals.pre_save.connect(movie_pre_save_reciever, sender=Movie)