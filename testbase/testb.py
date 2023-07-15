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


class TestB:

    def checkClass(self):
        """this method will check if the subclass meet the requirements
        or no.
        1 - one checking if one exist or no
        2 - checking if its constructor has exactly 1 parameter"""
        className = TestB.__subclasses__()  # here we are getting the name of the subclass
        if len(className) == 1:  # making sure there is exactly one subclass
            className = className[0]
        else:
            raise

    def getAllMethodNames(self):
        """this method will get all the method names of the
        subclass"""

        className = TestB.__subclasses__()[0]  # here we are getting the name of the subclass
