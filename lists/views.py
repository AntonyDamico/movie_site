from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import List
from movies.models import Movie

@login_required
def movie_list_view(request):
    user_movies = request.user.list.get_user_movies()
    context = {'movies': user_movies}
    return render(request, 'lists/list.html', context)

