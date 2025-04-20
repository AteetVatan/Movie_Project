"""The MovieFlaskView Module."""
from io import StringIO
import pycountry
from flask import render_template, flash

from helpers import PrintInputHelper as Ph
from constants import ConstantStrings as Cs
from constants.data_constants import DataConstants as Dc
from config import config


class MovieFlaskView():
    """Flask view implementation for movie application."""

    # region CREATE
    def data_added(self, new_movie: str) -> None:
        # Flash message will be handled by Flask's flash system
        pass

    # endregion CREATE

    # region READ
    def movie_list_data(self, data: dict) -> None:
        return render_template('movie_list.html', movies=data)

    def random_movie(self, random_movie_data: dict) -> None:
        return render_template('random_movie.html', movie=random_movie_data)

    def display_search_data(self, result_found: list) -> None:
        return render_template('search_results.html', results=result_found)

    def display_sorted_data(self, sorted_list: list) -> None:
        return render_template('sorted_movies.html', movies=sorted_list)

    def display_filtered_data(self, filtered_data: list) -> None:
        return render_template('filtered_movies.html', movies=filtered_data)

    def display_data_stats(self, best_movies: list, worst_movies: list, 
                          avg_rating: float, median_rating: float) -> None:
        return render_template('movie_stats.html', 
                             best_movies=best_movies,
                             worst_movies=worst_movies,
                             avg_rating=avg_rating,
                             median_rating=median_rating)

    def generate_website(self, data: dict, html_handler) -> None:
        # This functionality is handled by Flask's template system
        pass

    @staticmethod
    def __generate_website_html(data):
        # Assuming that we will have a very large string
        # So using StringIO
        string_buffer = StringIO()
        for k, v in data.items():
            title = v.get(Dc.title(), "")
            year = v.get(Dc.year(), "")
            poster = v.get(Dc.poster(), "")
            notes = v.get(Dc.notes(), "")
            rating = v.get(Dc.rating(), 0)
            imdb_page = config.OMDB_API_IMDB_PAGE.format(KEY=k)
            
            country_list = v.get(Dc.country(), "unknown")
            if isinstance(country_list, list):
                country = country_list[0].strip()
            else:
                country = country_list.split(",")[0].strip()            
            country = country 
            string_buffer.write(MovieFlaskView.__generate_movie_li(title=title,
                                                              year=year,
                                                              poster=poster,
                                                              notes=notes,
                                                              rating=rating,
                                                              imdb_page=imdb_page,
                                                              country=country))

        return string_buffer.getvalue()

    @staticmethod
    def __generate_movie_li(**kwargs):
        """Method to generate an HTML list with movie title, year, poster."""
        title = kwargs.get(Dc.title(), "")
        year = kwargs.get(Dc.year(), Cs.NOT_AVAILABLE)
        poster = kwargs.get(Dc.poster(), "")
        notes = kwargs.get(Dc.notes(), "")
        rating = kwargs.get(Dc.rating(), Cs.NOT_AVAILABLE)
        imdb_page = kwargs.get("imdb_page", "")
        country = kwargs.get(Dc.country(), Cs.NOT_AVAILABLE)

        rating_stars = MovieFlaskView.__generate_movie_rating_stars(rating)
        flag = MovieFlaskView.__get_flag(country)
        return f'''
                <li>
                    <div class="movie">
                        <a href="{imdb_page}" target="_blank">
                            <img class="movie-poster" src="{poster}" title="{notes}">
                        </a>                        
                        <div class="movie-title">
                            {title}
                        </div>
                        <div class="movie-title">
                            <img src="{flag}" title="{country}" class="flag-icon">
                        </div>
                        <div class="movie-year">{year}</div>
                        <div class="movie-rating" title="{rating}">{rating_stars}</div>
                    </div>
                </li>'''

    @staticmethod
    def __generate_movie_rating_stars(rating):
        """Method to generate stars for rating."""
        try:
            rating = float(rating)
        except ValueError:
            rating = 0

        stars = round((rating / 10) * 5)
        return "★" * stars + "☆" * (5 - stars)

    @staticmethod
    def __get_flag(country_name):
        """Method gets the flag for the given country name."""
        country = pycountry.countries.get(name=country_name)  # get country ISO code
        if country:
            return f"flags/{country.alpha_2.lower()}.png"
        return ""

    def render_home_page(self, title: str, movies: dict, search_placeholder: str):
        """Render the home page with movies and navigation.
        
        Args:
            title: Page title
            movies: Dictionary of movies where key is movie ID and value is movie data
            search_placeholder: Placeholder text for search input
        """
       
        
        return render_template('home.html',
                            title=title,
                            movies=movies,
                            search_placeholder=search_placeholder)

    # endregion READ

    # region UPDATE
    def update_movie_complete(self, update_movie_name: str) -> None:
        # Flash message will be handled by Flask's flash system
        pass

    def save_movie_data_complete(self) -> None:
        # Flash message will be handled by Flask's flash system
        pass

    # endregion UPDATE

    # region DELETE
    def movie_delete_complete(self, title: str) -> None:
        # Flash message will be handled by Flask's flash system
        pass

    # endregion DELETE

    def movie_error(self, error: str) -> None:
        # Flash message will be handled by Flask's flash system
        pass

    def movie_msg(self, message: str) -> None:
        # Flash message will be handled by Flask's flash system
        pass
