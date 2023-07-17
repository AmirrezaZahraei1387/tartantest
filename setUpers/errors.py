
class BothSetupTakedownError(Exception):
    """this error occurs when one of the setups or
    takedowns are not provided by the user"""

    def __init__(self, msg):

        super().__init__(msg)