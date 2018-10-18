def format_movie(qs_movie):
    new_movie_title = qs_movie.POST.get('title')
    new_movie_year = qs_movie.POST.get('year')
    new_movie_poster = qs_movie.POST.get('poster')
    new_movie = {
        'title': new_movie_title,
        'year': new_movie_year,
        'poster': new_movie_poster
    }
    return new_movie