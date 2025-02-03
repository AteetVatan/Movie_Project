"""The main Module."""
from base.movies_controller import MoviesController
from data.data_handler import DataHandler
from helpers.main_print import MainPrint, MainPrintEnum


def main():
    """The Main wrapper function."""
    movies = DataHandler.read_data()
    movie_obj = MoviesController(movies)
    initialize_user_menu(movie_obj)


def initialize_user_menu(movie_obj: MoviesController) -> None:
    """Function to initialize the User Menu"""
    menu_length = movie_obj.get_menu_items_length
    menu_index = 0
    MainPrint.pr_menu(MainPrint.get_prompt_string(MainPrintEnum.WELCOME.value))
    while True:
        display_menu(movie_obj)
        print("\n")
        user_input = MainPrint.pr_input(
            MainPrint.get_prompt_string(MainPrintEnum.ENTER_CHOICE.value, key1=menu_length))
        if is_valid_menu_input(user_input, menu_length):
            menu_index = int(user_input)
            if user_operations(movie_obj, menu_index):
                break
            MainPrint.pr_input(MainPrint.get_prompt_string(MainPrintEnum.CONTINUE.value))
        else:
            MainPrint.pr_error(MainPrint.get_prompt_string(MainPrintEnum.INVALID.value))
            continue


def is_valid_menu_input(user_input: str, menu_length: int) -> bool:
    """Function for menu input validation."""
    menu_length += 1
    if user_input.isdigit() and 1 <= int(user_input) <= menu_length:
        return True
    return False


def display_menu(movie_obj: MoviesController) -> None:
    """Function to display menu."""
    menu_items = movie_obj.get_menu_items_descriptions
    print("\n")
    MainPrint.pr_menu(MainPrint.get_prompt_string(MainPrintEnum.MENU.value))

    for item in enumerate(menu_items):
        print(f"{item[0] + 1}. {item[1]}")


def user_operations(movie_obj: MoviesController, menu_index: int) -> bool:
    """Function for User Operations"""
    method = movie_obj.menu_manager.get_menu_method_by_index(menu_index)
    kwargs = movie_obj.menu_manager.get_menu_arguments_by_index(menu_index)
    return method(**kwargs)


if __name__ == "__main__":
    main()
