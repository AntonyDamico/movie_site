# pylint: disable=E1101
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
# from django.http import JsonResponse

from rest_framework import generics
from .serializers import MovieSerializer

from .models import Movie

# class MovieListView(generic.ListView):
#     queryset = Movie.objects.all()
#     template_name = 'movies/list.html'
#     context_object_name = 'movies'

# class MovietDetailSlugView(generic.DetailView):
#     queryset = Movie.objects.all()
#     template_name = 'movies/detail.html'
#     context_object_name = 'movies'

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovietDetailSlugView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'