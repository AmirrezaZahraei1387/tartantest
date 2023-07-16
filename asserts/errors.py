

class FailAssertionError(BaseException):
    """this error will be raised when the assertion went wrong,
    and it evaluates to the thing that we did not want."""
    def __init__(self, statement: str, value1,
                 value2, formattingStatement: str,
                 assertionName: str, description: str):
        """the statement is the statement in the function for checking the values
        value 1 and value2 are the values of assertion
        formattingStatement is the statement for formatting the values to show the condition
        assertionName is the name of assertion that occurs
        description is the message about what have happened"""
        message = "\n"
        message += statement+'\n'
        message += formattingStatement.format(str(value1), str(value2))+'\n'
        message += assertionName+":"+description+'\n'

        super().__init__(message)







