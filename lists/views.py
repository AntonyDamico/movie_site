# pylint: disable=E1101
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import ListSerializer
from movies.serializers import MovieSerializer
from .models import List
from movies.models import Movie
from .forms import MovieForm
from .utils import format_movie


# @login_required
# def movie_list_view(request):
#     user = request.user
#     user_movies = user.list.get_user_movies()
#     for movie in user_movies:
#         movie.user_rating = movie.get_user_rating(user)
#     context = {'movies': user_movies}
#     return render(request, 'lists/list.html', context)


@api_view(['GET'])
def movie_list_view(request):
    user = request.user
    if request.method == 'GET':
        user_movies = user.list.get_user_movies()
        # for movie in user_movies:
        #     movie.user_rating = movie.get_user_rating(user)
        serializer = MovieSerializer(user_movies, many=True)
        return Response(serializer.data)


@login_required
def add_movie_to_list_view(request):
    form = MovieForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        new_movie = format_movie(request.POST)
        user_list = request.user.list
        user_list.add_movie_to_list(new_movie)
        return redirect('list:index')
    return render(request, 'lists/add_movie.html', context)


def delete_movie_from_list_view(request, movie_id):
    user_list = request.user.list
    movie = get_object_or_404(Movie, pk=movie_id)
    if user_list.movie_in_list(movie):
        user_list.remove_movie_from_list(movie)
        return redirect('list:index')
    return redirect('list:index')
