"""The MovieView Module."""
from io import StringIO
import pycountry

from helpers import PrintInputHelper as Ph
from constants import ConstantStrings as Cs
from constants.data_constants import DataConstants as Dc
from models.html_file_handler_model import HtmlFileHandlerModel
from config import config


class MovieView:
    """The MovieView Class."""

    # region CREATE
    @staticmethod
    def data_added(new_movie: str):
        """Method to add data."""
        Ph.pr_menu(Cs.MOVIE_ADDED.format(KEY1=new_movie))

    # endregion CREATE

    # region READ
    @staticmethod
    def movie_list_data(data):
        """Method to list Movie data."""
        movie_length = len(data)
        Ph.pr_bold(Cs.MOVIE_TOTAL.format(KEY1=movie_length))
        for item in data.values():
            title = item.get(Dc.title(), Cs.NOT_AVAILABLE)
            year = item.get(Dc.year(), Cs.NOT_AVAILABLE)
            rating = item.get(Dc.rating(), Cs.NOT_AVAILABLE)
            rating = rating if rating == Cs.NOT_AVAILABLE else f"{float(rating):.2f}"
            Ph.pr_menu(f"\t{title} ({year}): {rating}")

    @staticmethod
    def random_movie(random_movie_data):
        """Prints random Movies."""
        title = random_movie_data[Dc.title()]
        rating = float(random_movie_data[Dc.rating()])
        Ph.pr_menu(
            (Cs.MOVIE_CHOSEN.format(KEY1=title,
                                    KEY2=f"{rating:.2f}")))

    @staticmethod
    def display_search_data(search_result: list):
        """Prints searched Result."""
        for item in search_result:
            Ph.pr_menu(f"\t{item[0].title()}, {item[1]}")

    @staticmethod
    def display_sorted_data(sorted_list: list):
        """Prints searched Result."""
        for item in sorted_list:
            Ph.pr_menu(f"{item[0]}: {item[1]}")

    @staticmethod
    def display_filtered_data(filtered_data: list):
        """Prints filtered Result."""
        for item in filtered_data:
            Ph.pr_menu(f"\t{item[0]} ({item[2]}): {item[1]}")

    @staticmethod
    def display_data_stats(best_movies: list,
                           worst_movies: list,
                           avg_rating: float,
                           median_rating: float):
        """Prints data statistics."""
        Ph.pr_menu(Cs.AVG_RATING.format(KEY1=f"{avg_rating:.2f}"))
        Ph.pr_menu(Cs.MEDIAN_RATING.format(KEY1=f"{median_rating:.2f}"))
        for item in best_movies:
            Ph.pr_menu(Cs.MOVIE_BEST.format(
                KEY1=item[Dc.title()], KEY2=item[Dc.rating()]))
        for item in worst_movies:
            Ph.pr_menu(Cs.MOVIE_WORST.format(
                KEY1=item[Dc.title()], KEY2=item[Dc.rating()]))

    @staticmethod
    def generate_website(data, html_file_handler: HtmlFileHandlerModel):
        """Method to generate_website."""
        template_data = html_file_handler.html_template_data
        # set website title
        website_title = config.HTML_WEB_PAGE_TITLE
        website_title_anchor = config.HTML_TEMPLATE_TITLE_ANCHOR
        web_page = template_data.replace(website_title_anchor, website_title)
        # Get The HTML from data
        website_movie_grid_anchor = config.HTML_TEMPLATE_MOVIE_GRID_ANCHOR
        web_html = MovieView.__generate_website_html(data)
        web_page = web_page.replace(website_movie_grid_anchor, web_html)
        html_file_handler.write_html_data(web_page)
        Ph.pr_menu(f"Website [{html_file_handler.file_name}] was generated successfully.")

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
            country = v.get(Dc.country(), "").split(",")[0].strip()
            string_buffer.write(MovieView.__generate_movie_li(title=title,
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

        rating_stars = MovieView.__generate_movie_rating_stars(rating)
        flag = MovieView.__get_flag(country)
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

        # endregion READ

    # region UPDATE
    @staticmethod
    def update_movie_complete(update_movie_name):
        """Prints update_movie_complete success."""
        Ph.pr_menu(Cs.MOVIE_UPDATED.format(KEY1=update_movie_name))

    @staticmethod
    def save_movie_data_complete():
        """Prints save data success."""
        Ph.pr_menu(Cs.MOVIE_DATA_SAVED)

    # endregion UPDATE

    # region DELETE
    @staticmethod
    def movie_delete_complete(title: str):
        """View method to show delete operation method output."""
        Ph.pr_menu(Cs.MOVIE_DELETE_DONE.format(KEY1=title))

    # endregion DELETE

    @staticmethod
    def movie_error(error: str):
        """View method to show error."""
        Ph.pr_error(error)

    @staticmethod
    def movie_msg(mgg: str):
        """View method to show a message."""
        Ph.pr_bold(mgg)
