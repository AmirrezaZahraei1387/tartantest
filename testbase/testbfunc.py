"""this is a file named testbfunc that give you the option to run your
tests as functions instead of classes. it has decorator that you should decorate
the function you want with. it has a list that will save all your
test functions and then when you use the method run
it will run all the functions to be tested.
you do not need to put a special name at the first of function
names."""
import inspect
import time
import traceback
from termcolor import colored
import errors
from testbclass import getParameterNumber


class TestBFunc:

    __functions: list = []

    def addFunc(self, function):
        """this is the decorator that will get the
        function and save the function to run for
        test."""
        self.checkFunc(function=function)
        self.__functions.append(function)
        return function

    @staticmethod
    def checkFunc(function):
        """the checkFunc checks the number of parameters the
        function have. if it has zero parameters it path otherwise the
        method will raise an error"""

        parameterNumber = getParameterNumber(function)
        if parameterNumber > 0:
            raise errors.TooManyParametersError("expected no parameters for "+str(function))
        return function







