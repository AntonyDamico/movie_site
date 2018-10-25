from django.urls import path

from . import views
from ratings.views import rate_movie_view

app_name = 'list'

urlpatterns = [
    path('', views.movie_list_view, name='index'),
    path('create', views.add_movie_to_list_view, name='add_movie'),
    path('<int:movie_id>/delete',
         views.delete_movie_from_list_view, name='delete_movie'),
    path('<int:movie_id>/vote', rate_movie_view, name='rate_movie')
]
