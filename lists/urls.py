from django.urls import path

from . import views

app_name = 'list'

urlpatterns = [
    path('', views.movie_list_view, name='index'),
    path('<int:movie_id>/delete', views.delete_movie_from_list, name='delete_movie')
]