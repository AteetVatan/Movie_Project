"""The MovieCliView Module."""
from io import StringIO
import pycountry

from helpers import PrintInputHelper as Ph
from constants import ConstantStrings as Cs
from constants.data_constants import DataConstants as Dc
from config import config


class MovieCliView():
    """CLI view implementation for movie application."""

    # region CREATE
    def data_added(self, new_movie: str) -> None:
        """Method to add data."""
        Ph.pr_menu(Cs.MOVIE_ADDED.format(KEY1=new_movie))

    # endregion CREATE

    # region READ
    def movie_list_data(self, data: dict) -> None:
        """Method to list Movie data."""
        movie_length = len(data)
        Ph.pr_bold(Cs.MOVIE_TOTAL.format(KEY1=movie_length))
        for item in data.values():
            title = item.get(Dc.title(), Cs.NOT_AVAILABLE)
            year = item.get(Dc.year(), Cs.NOT_AVAILABLE)
            rating = item.get(Dc.rating(), Cs.NOT_AVAILABLE)
            rating = rating if rating == Cs.NOT_AVAILABLE else f"{float(rating):.2f}"
            Ph.pr_menu(f"\t{title} ({year}): {rating}")

    def random_movie(self, random_movie_data: dict) -> None:
        """Prints random Movies."""
        title = random_movie_data[Dc.title()]
        rating = float(random_movie_data[Dc.rating()])
        Ph.pr_menu(
            (Cs.MOVIE_CHOSEN.format(KEY1=title,
                                    KEY2=f"{rating:.2f}")))

    def display_search_data(self, result_found: list) -> None:
        """Prints searched Result."""
        for title, rating in result_found:
            Ph.pr_menu(f"\t{title}, {rating}")

    def display_sorted_data(self, sorted_list: list) -> None:
        """Prints searched Result."""
        for title, rating in sorted_list:
            Ph.pr_menu(f"{title}: {rating}")

    def display_filtered_data(self, filtered_data: list) -> None:
        """Prints filtered Result."""
        for title, rating, year in filtered_data:
            Ph.pr_menu(f"\t{title} ({year}): {rating}")

    def display_data_stats(self, best_movies: list, worst_movies: list, 
                          avg_rating: float, median_rating: float) -> None:
        """Prints data statistics."""
        Ph.pr_menu(Cs.AVG_RATING.format(KEY1=f"{avg_rating:.2f}"))
        Ph.pr_menu(Cs.MEDIAN_RATING.format(KEY1=f"{median_rating:.2f}"))
        print("\nBest Movies:")
        for movie in best_movies:
            Ph.pr_menu(Cs.MOVIE_BEST.format(
                KEY1=movie[Dc.title()], KEY2=movie[Dc.rating()]))
        print("\nWorst Movies:")
        for movie in worst_movies:
            Ph.pr_menu(Cs.MOVIE_WORST.format(
                KEY1=movie[Dc.title()], KEY2=movie[Dc.rating()]))

    def generate_website(self, data: dict, html_handler) -> None:
        """Method to generate_website."""
        template_data = html_handler.html_template_data
        # set website title
        website_title = config.HTML_WEB_PAGE_TITLE
        website_title_anchor = config.HTML_TEMPLATE_TITLE_ANCHOR
        web_page = template_data.replace(website_title_anchor, website_title)
        # Get The HTML from data
        website_movie_grid_anchor = config.HTML_TEMPLATE_MOVIE_GRID_ANCHOR
        web_html = self.__generate_website_html(data)
        web_page = web_page.replace(website_movie_grid_anchor, web_html)
        html_handler.write_html_data(web_page)
        Ph.pr_menu(f"Website [{html_handler.file_name}] was generated successfully.")

    def __generate_website_html(self, data):
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
            string_buffer.write(self.__generate_movie_li(title=title,
                                                              year=year,
                                                              poster=poster,
                                                              notes=notes,
                                                              rating=rating,
                                                              imdb_page=imdb_page,
                                                              country=country))

        return string_buffer.getvalue()

    def __generate_movie_li(self, **kwargs):
        """Method to generate an HTML list with movie title, year, poster."""
        title = kwargs.get(Dc.title(), "")
        year = kwargs.get(Dc.year(), Cs.NOT_AVAILABLE)
        poster = kwargs.get(Dc.poster(), "")
        notes = kwargs.get(Dc.notes(), "")
        rating = kwargs.get(Dc.rating(), Cs.NOT_AVAILABLE)
        imdb_page = kwargs.get("imdb_page", "")
        country = kwargs.get(Dc.country(), Cs.NOT_AVAILABLE)

        rating_stars = self.__generate_movie_rating_stars(rating)
        flag = self.__get_flag(country)
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

    def __generate_movie_rating_stars(self, rating):
        """Method to generate stars for rating."""
        try:
            rating = float(rating)
        except ValueError:
            rating = 0

        stars = round((rating / 10) * 5)
        return "★" * stars + "☆" * (5 - stars)

    def __get_flag(self, country_name):
        """Method gets the flag for the given country name."""
        country = pycountry.countries.get(name=country_name)  # get country ISO code
        if country:
            return f"flags/{country.alpha_2.lower()}.png"
        return ""

    # endregion READ

    # region UPDATE
    def update_movie_complete(self, update_movie_name: str) -> None:
        """Prints update_movie_complete success."""
        Ph.pr_menu(Cs.MOVIE_UPDATED.format(KEY1=update_movie_name))

    def save_movie_data_complete(self) -> None:
        """Prints save data success."""
        Ph.pr_menu(Cs.MOVIE_DATA_SAVED)

    # endregion UPDATE

    # region DELETE
    def movie_delete_complete(self, title: str) -> None:
        """View method to show delete operation method output."""
        Ph.pr_menu(Cs.MOVIE_DELETE_DONE.format(KEY1=title))

    # endregion DELETE

    def movie_error(self, error: str) -> None:
        """View method to show error."""
        Ph.pr_error(error)

    def movie_msg(self, message: str) -> None:
        """View method to show a message."""
        Ph.pr_bold(message)
