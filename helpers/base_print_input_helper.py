"""Module for prints and inputs"""


class PrintInputHelper:
    """Class Wrapper for input string and custom color inputs, printing"""
    _prompt_dictionary = {}

    @classmethod
    def get_prompt_string(cls, prompt_key, **kwargs):
        """Returns the cosole display string"""
        item_str = cls._prompt_dictionary[prompt_key]
        if kwargs:
            return item_str.format(**kwargs)
        return item_str

    @staticmethod
    def pr_menu(txt):
        """Prints the Menu items in teal color."""
        print("\033[38;5;37m" + txt + "\033[0m")

    @staticmethod
    def pr_error(txt):
        """Print error messages in red"""
        print("\033[91m" + txt + "\033[0m")

    @staticmethod
    def pr_bold(txt):
        """Prints text in bold"""
        print("\033[1m" + txt + "\033[0m")

    @staticmethod
    def pr_input(txt):
        """Print input prompt in a brownish color (yellow)"""
        return input("\033[33m" + txt + "\033[0m").strip()
