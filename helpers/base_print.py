"""Wrapper Module for prints and inputs"""


class BasePrint:
    """Class Wrapper for input string and custom colour inputs, printing"""
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
        """Prints the Menu items"""
        print("\033[93m {}\033[00m".format(txt))

    @staticmethod
    def pr_error(txt):
        """Prints the Error"""
        print("\033[93m {}\033[00m".format(txt))

    @staticmethod
    def pr_input(txt):
        """Prints the text for Input"""
        return input("\033[92m {}\033[00m".format(txt))
