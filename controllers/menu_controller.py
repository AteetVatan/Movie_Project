"""Module for Menu Controller."""
from constants import ConstantStrings
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
