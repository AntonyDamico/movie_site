from django.contrib import admin
from .models import Rating, UserRating

admin.site.register(Rating)
admin.site.register(UserRating)
