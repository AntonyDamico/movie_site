# pylint: disable=E1101
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import List
from movies.models import Movie

@login_required
def movie_list_view(request):
    user_movies = request.user.list.get_user_movies()
    context = {'movies': user_movies}
    return render(request, 'lists/list.html', context)

def delete_movie_from_list(request, movie_id):
    user_list = request.user.list
    movie = get_object_or_404(Movie, pk=movie_id)
    # return HttpResponse(user.list.movie_in_list(movie))
    if user_list.movie_in_list(movie):
        movie.delete()
        return redirect('list:index')
    return redirect('list:index')