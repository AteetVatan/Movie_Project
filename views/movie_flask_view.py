"""The MovieFlaskView Module."""
from flask import render_template


class MovieFlaskView:
    """Flask view implementation for movie application."""

    # region CREATE
    # endregion CREATE

    # region READ
    def render_home_page(self, title: str, movies: dict, search_placeholder: str):
        """Render the main home page with movie listings."""
        return render_template('home.html',
                               title=title,
                               movies=movies,
                               search_placeholder=search_placeholder)

    def movie_list_data(self, data: dict) -> None:
        """Display a list of all movies."""
        return render_template('movie_list.html', movies=data)

    def random_movie(self, random_movie_data: dict) -> None:
        """Display a randomly selected movie."""
        return render_template('random_movie.html', movie=random_movie_data)

    def display_search_data(self, result_found: list) -> None:
        """Show search results for movies."""
        return render_template('search_results.html', results=result_found)

    def display_sorted_data(self, sorted_list: list) -> None:
        """Display movies in sorted order."""
        return render_template('sorted_movies.html', movies=sorted_list)

    def display_filtered_data(self, filtered_data: list) -> None:
        """Show filtered movie results."""
        return render_template('filtered_movies.html', movies=filtered_data)

    def display_data_stats(self, best_movies: list, worst_movies: list,
                           avg_rating: float, median_rating: float) -> None:
        """Display movie statistics including ratings and rankings."""
        return render_template('movie_stats.html',
                               best_movies=best_movies,
                               worst_movies=worst_movies,
                               avg_rating=avg_rating,
                               median_rating=median_rating)
    # endregion READ

    # region UPDATE
    # endregion UPDATE

    # region DELETE
    # endregion DELETE
