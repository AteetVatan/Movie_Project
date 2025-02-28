"""The Menu Output type module."""


class MenuOperationOutputModel:
    """The Menu Output type class."""

    def __init__(self, operation_wait=True, operation_exit=False):
        self.operation_wait = operation_wait
        self.operation_exit = operation_exit
