# pylint: disable=E1101
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import List
from movies.models import Movie
from .forms import MovieForm
from .utils import format_movie

@login_required
def movie_list_view(request):
    user_movies = request.user.list.get_user_movies()
    context = {'movies': user_movies}
    return render(request, 'lists/list.html', context)

@login_required
def add_movie_to_list_view(request):
    form = MovieForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        # maybe just remove the csfr token from request.POST instead of formating it
        new_movie = format_movie(request.POST)
        user_list = request.user.list
        user_list.add_movie_to_list(new_movie)
        return redirect('list:index')
    return render(request, 'lists/add_movie.html', context)

# TODO: change the delete method, it deletes the movie from all lists, not just form the user's list
def delete_movie_from_list_view(request, movie_id):
    user_list = request.user.list
    movie = get_object_or_404(Movie, pk=movie_id)
    if user_list.movie_in_list(movie):
        movie.delete()
        return redirect('list:index')
    return redirect('list:index')