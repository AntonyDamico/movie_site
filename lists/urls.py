from django.urls import path

from . import views

app_name = 'list'

urlpatterns = [
    path('', views.movie_list_view, name='index'),
    path('create', views.add_movie_to_list_view, name='add_movie'),
    path('<int:movie_id>/delete', views.delete_movie_from_list_view,name='delete_movie')
]