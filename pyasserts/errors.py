

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
        self.message = "\n"
        self.message += statement+'\n'
        self.message += formattingStatement.format(str(value1), str(value2))+'\n'
        self.message += assertionName+":"+description+'\n'

        super().__init__(self.message)


class preFailError(BaseException):
    """this error is raised when we want to fail a test with
    no condition. it can have two different conditions fail one test or
    failing all the tests in the class."""

    modes = ["failtest", "failall"]

    def __init__(self, failingMode: str, description: str):
        """the failingMode can have two different values FAILALL or FAIL-TEST.
        FAIL_ALL will fail all the tests in the class while FAILTEST means to fail
        the current test. this class won't do these things and these values will
        be read with the base classes,and they do that."""

        if failingMode.lower() not in self.modes:
            raise TypeError("expected values "+str(self.modes)+" for failingMode")

        self.failingMode = failingMode
        self.message = description+'\n'+"failingMode: "+self.failingMode
        super().__init__(self.message)





