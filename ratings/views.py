from django.shortcuts import render, get_object_or_404, redirect

from .models import UserRating
from movies.models import Movie

def rate_movie_view(request, movie_id):
    user = request.user
    user_rating = request.POST.get('user_rating')
    movie = get_object_or_404(Movie, pk=movie_id)
    UserRating.objects.rate_new_movie(user, movie, user_rating)
    return redirect('list:index')

