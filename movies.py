"""The main Module."""
from controllers import MenuController
from enumerations import AppTypes


def main():
    """The Main wrapper function."""
    menu_controller = MenuController(AppTypes.MOVIE)
    menu_controller.start()


if __name__ == "__main__":
    main()
