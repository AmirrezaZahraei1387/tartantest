

class NotOneSubClassError(Exception):
    """this error is raised when the user have more than one or zero
    subclasses for the test class."""

    def __init__(self, message):
        super().__init__(message)


class TooManyParametersError(Exception):
    """this error is raised when the subclasses that are provided have
    more than 1 parameter or have no parameter"""

    def __init__(self, message):
        super().__init__(message)