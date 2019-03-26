import os
import webbrowser


# Styles and scripting for the page
html_head = open('./templates/head.html')
head_template = html_head.read()
html_head.close()

# template for body of the html page which includes the trailer as well as
# the movie cards
html_body = open('./templates/body.html')
body_template = html_body.read()
html_body.close()

# template for each movie card
html_card = open('./templates/card.html')
card_template = html_card.read()
html_card.close()


def render_card_content(movie):
    """
    Formats the card template with the movie data.

    Args:
        (Movie) movie - the details related to the movie.
    Returns:
        (str) the formatted card template as a string.
    """
    return card_template.format(
        movie_mpaa_rating=movie.mpaa_rating,
        movie_title=movie.title,
        poster_image_url=movie.poster_image_url,
        release_date=movie.release_date,
        movie_plot=movie.plot,
        movie_genre=movie.genre,
        trailer_youtube_id=movie.youtube_id
    )


def render_movie_cards(movies):
    """
    Renders the template for all the movie details cards.

    Args:
        (list of Movie) movies - list of all the movies.
    Returns:
        (str) the movie details cards template as a string.
    """
    return "".join(map(render_card_content, movies))


def render_page_html(movies):
    """
    Renders the html template.

    Args:
        (list of Movie) movies - list of all the movies.
    Returns:
        (str) the formatted html template as a string.
    """
    return head_template + body_template.format(
        movie_cards=render_movie_cards(movies))


def open_movies_page(movies):
    """
    Renders the html template.

    Args:
        (list of Movie) movies - list of all the movies.
    Returns:
        (str) the formatted html template as a string.
    """
    # render_page_html(movies)
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    # write the renderd html content of the page to the file.
    output_file.write(render_page_html(movies))
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
