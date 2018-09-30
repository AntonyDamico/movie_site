from django.urls import path

from . import views

app_name = 'list'

urlpatterns = [
    path('', views.movie_list_view, name='index')
]