"""this is a file named testbfunc that give you the option to run your
tests as functions instead of classes. it has decorator that you should decorate
the function you want with. it has a list that will save all your
test functions and then when you use the method run
it will run all the functions to be tested.
you do not need to put a special name at the first of function
names."""

import testbase.errors as errors
from testbase.base import Base


class TestBFunc(Base):

    __functions: list = []

    def __init__(self, name: str):
        """the name parameter is the name of the test it is running.
        it is used to organize the tests results printed in console
        better, and it is a better idea to provide it with a meaningful
        name."""
        self.__name = name

        # the values for the __init__ of Base are not provided
        # because it needs all the functions we have, and at this point we do not now our functions
        # we provide it later in the run method
        super().__init__([])

    def addFunc(self, function):
        """this is the decorator that will get the
        function and save the function to run for
        test."""
        self.checkFunc(function=function)
        self.__functions.append(function)
        return function

    def checkFunc(self, function):
        """the checkFunc checks the number of parameters the
        function have. if it has zero parameters it path otherwise the
        method will raise an error"""

        parameterNumber = self.getParameterNumber(function)
        if parameterNumber > 0:
            raise errors.TooManyParametersError("expected no parameters for "+str(function.__name__))
        return function

    @staticmethod
    def makeFormatOkForBase(funcs):
        """because the Base class only will accept the for like this:
        # [(methodName, methodAddress), (methodName, methodAddress), ... ]
        we need to make it to avoid problems"""

        newFuncFor = []

        for func in funcs:
            newFuncFor.append((func.__name__, func))

        return newFuncFor

    def run(self):
        super().__init__(self.makeFormatOkForBase(self.__functions))
        print("***start running function tests named ", self.__name, "\n")
        for func in self.__functions:
            name = str(func.__name__)
            if name.startswith(self.names["setup"]) or name.startswith(self.names["takedown"]):
                pass
            else:
                self.runTest(func, func.__name__)
        print("***end running function tests named ", self.__name, "\n")
