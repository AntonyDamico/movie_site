from movies.models import Movie

def format_movie(qs_movie):
    new_title = qs_movie.get('title')
    new_year = qs_movie.get('year')
    new_poster = qs_movie.get('poster')
    new_movie = Movie(title=new_title, year=new_year, poster=new_poster)
    print('new movie', new_movie)
    return new_movie