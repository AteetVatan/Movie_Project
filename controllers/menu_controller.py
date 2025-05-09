"""Module for Menu Controller."""
from constants import ConstantStrings, DataConstants as Jc
from controllers.base_controller import BaseController
from helpers import PrintInputHelper as bp
from models import MenuOperationOutputModel


class MenuController:
    """Class for Menu."""
    __controller_obj = None

    def __init__(self, controller_obj: BaseController):
        self.__controller_obj = controller_obj

    @property
    def controller(self):
        """Property to get the controller instance."""
        return self.__controller_obj

    def start(self):
        """Method to start the controller."""
        MenuController.initialize_user_menu(self.__controller_obj)

    @staticmethod
    def initialize_user_menu(controller_obj) -> None:
        """Function to initialize the User Menu"""
        menu_length = controller_obj.get_menu_items_length
        while True:
            try:
                MenuController.display_menu(controller_obj)
                user_input = bp.pr_input(ConstantStrings.
                                         MAIN_PRINT_ENTER_CHOICE.format(key1=menu_length))
                if not user_input:
                    continue

                if MenuController.is_valid_menu_input(user_input, menu_length):
                    menu_index = int(user_input)
                    menu_output: MenuOperationOutputModel = (
                        MenuController.user_operations(controller_obj, menu_index))
                    if menu_output.operation_exit:
                        break
                    if menu_output.operation_wait:
                        bp.pr_input(ConstantStrings.MAIN_PRINT_CONTINUE)
                else:
                    bp.pr_error(ConstantStrings.MAIN_PRINT_INVALID)
                    continue
            except (ValueError, TypeError) as e:
                raise ValueError(f"initialize_user_menu Error: {e.args[0]}") from e
            except Exception as e:
                raise RuntimeError("initialize_user_menu Error: " +
                                   ConstantStrings.GENERAL_ERROR.format(error=e)) from e

    @staticmethod
    def is_valid_menu_input(user_input: str, menu_length: int) -> bool:
        """Function for menu input validation."""
        menu_length += 1
        if user_input.isdigit() and 1 <= int(user_input) <= menu_length:
            return True
        return False

    @staticmethod
    def display_menu(controller_obj) -> None:
        """Function to display a menu."""
        menu_items = controller_obj.get_menu_items_descriptions
        bp.pr_bold(ConstantStrings.MAIN_PRINT_MENU)

        for item in enumerate(menu_items):
            bp.pr_menu(f"\t{item[0] + 1}. {item[1]}")

    @staticmethod
    def user_operations(controller_obj, menu_index: int) -> bool:
        """Function for User Operations"""
        method = controller_obj.menu_manager.get_menu_method_by_index(menu_index)
        kwargs = controller_obj.menu_manager.get_menu_arguments_by_index(menu_index)
        return method(**kwargs)

    # region private-methods
    @staticmethod
    def get_menu_dictionary(controller_obj, data_desc) -> dict:
        """The Menu methods initialization."""
        return {
            1: {"method": controller_obj.exit, "desc": "Exit".title()},
            2: {"method": controller_obj.list_data, "desc": f"List {data_desc}s".title()},
            3: {"method": controller_obj.add_data, "desc": f"Add {data_desc}".title()},
            4: {"method": controller_obj.delete_data, "desc": f"Delete {data_desc}".title()},
            5: {"method": controller_obj.update_data, "desc": f"Update {data_desc}".title()},
            6: {"method": controller_obj.data_stats, "desc": "Stats".title()},
            7: {"method": controller_obj.show_random_item_in_data,
                "desc": f"Random {data_desc}".title()},
            8: {"method": controller_obj.search_data, "desc": f"Search {data_desc}".title()},
            9: {"method": controller_obj.sort_data, "kwargs": {"key": Jc.rating()},
                "desc": f"{data_desc}s sorted by {Jc.rating()}".title()},
            10: {"method": controller_obj.sort_data, "kwargs": {"key": Jc.year()},
                 "desc": f"{data_desc}s sorted by {Jc.year()}".title()},
            11: {"method": controller_obj.data_filter, "desc": f"filter {data_desc}".title()},
            12: {"method": controller_obj.show_data_histogram,
                 "desc": f"Show {data_desc}s Histogram".title()},
            13: {"method": controller_obj.save_data, "desc": "Save".title()},
            14: {"method": controller_obj.generate_website, "desc": "Generate website"}
        }
    # endregion private-methods
