"""the testb is a file that is implemented to make
the most important part of the library.
this file will have a class named TestB that can be inherited from
the class containing the tests. it will run the tests.
the class will run the tests by getting the names of
methods inside that starts with test word. this because of
this reason to find the methods that are not tests and probably
have parameters."""
import warnings
import time
import inspect
import errors


class TestB:

    @staticmethod
    def checkClass():
        """this method will check if the subclass meet the requirements
        or no.
        1 - one checking if one exist or no
        2 - checking if its constructor has exactly 1 parameter"""

        className = TestB.__subclasses__()  # here we are getting the name of the subclass
        if len(className) is 1:  # making sure there is exactly one subclass
            className = className[0]
        else:
            raise errors.NotOneSubClassError("expected exactly one subclass got "+str(className))

        parameters = inspect.signature(className).parameters
        if len(parameters) is not 1:    # check if the __init__ have more than or less than 1 parameter
            raise errors.TooManyParametersError("expected one parameter got "+str(parameters))

        return className

    @staticmethod
    def getAllMethodNames(className):
        """this method will get all the method names of the
        subclass given as className"""
        inspect.getmembers()



