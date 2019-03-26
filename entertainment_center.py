import fresh_tomatoes
import media
import movies


def initialize_movie(movie_data):
    """
    Initializes an instance of the Movie class with the provided data.

    Args:
        (dict) movie_data - details of the movie.
    Returns:
        (Movie) movie - an instance of the Movie class with the provided data.
    """
    movie = media.Movie(
        movie_data['Title'],
        movie_data['Plot'],
        movie_data['Released'],
        movie_data['Rating'],
        movie_data['Genre'],
        movie_data['Poster'],
        movie_data['Trailer'])

    # set the youtube trailer id for the movie
    movie.set_youtube_trailer_id()

    return movie


# open the movie trailer website with the passed movie details
fresh_tomatoes.open_movies_page(map(initialize_movie, movies.MOVIE_LIST))
