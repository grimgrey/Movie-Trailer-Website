import re


class Movie():
    """
    A class used to represent a movie.

    Attributes:
        (str) title - name of the movie.
        (str) plot - brief plot of the movie.
        (str) release_date - date when the movie was released.
        (str) mapaa_rating - MPAA rating of the movie.
        (str) genre - genre of the movie.
        (str) poster_image_url - url for the poster of the movie.
        (str) trailer_youtube_url - url for the trailer of the movie.
        (str) youtube_id - youtube id for the trailer of the movie.

    Methods:
        set_youtube_trailer_id()
            Sets the youtube trailer id for the movie.
    """

    def __init__(
            self,
            movie_title,
            movie_plot,
            release_date,
            rating,
            genre,
            movie_poster,
            movie_trailer):
        self.title = movie_title
        self.plot = movie_plot
        self.release_date = release_date
        self.mpaa_rating = rating
        self.genre = genre
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def set_youtube_trailer_id(self):
        """
        Extracts the youtube id from the trailer url,
        and sets it as an instance variable
        """
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        self.youtube_id = (youtube_id_match.group(0) if youtube_id_match
                           else None)
