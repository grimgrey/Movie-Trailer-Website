import fresh_tomatoes
import media
import movies

movie_list = map(
    lambda movie_data: media.Movie(
        movie_data['Title'],
        movie_data['Plot'],
        movie_data['Poster'],
        movie_data['Trailer']),
    movies.MOVIE_LIST)

fresh_tomatoes.open_movies_page(movie_list)
