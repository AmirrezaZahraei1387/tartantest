

class TooManyParametersError(Exception):
    """this error is raised when the subclasses that are provided have
    more parameters or the method provided have parameters"""

    def __init__(self, message):
        super().__init__(message)