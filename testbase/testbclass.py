"""the testclass is a file that is implemented to make
the most important part of the library.
this file will have a class named TestBClass that can be inherited from
the class containing the tests. it will run the tests.
the class will run the tests by getting the names of
methods inside that starts with test word. this because of
this reason to find the methods that are not tests and probably
have parameters."""

import inspect
from tartantest import testbase as errors
import testbase as base

# this is the constants that defines the name that must come first in the method name of subclass that
# contain tests
STARTING_NAME = "testb"


class TestBClass(base.Base):

    def __init__(self):

        self.className = self.checkClass()  # if the subclass is not something we want error is raised
        self.allMethods = self.getAllMethodNames()    # the output is similar to this:
        # [(methodName, methodAddress), (methodName, methodAddress), ... ]
        self.allCurrentMethods = inspect.getmembers(object=self, predicate=inspect.ismethod)
        # getting all the methods no matter what it is

        super().__init__(self.allCurrentMethods)

    def checkClass(self):
        """this method will check if the subclass meet the requirements
        or no.
        checking if its constructor has exactly 1 parameter self"""
        className_ = self.__class__  # here we are getting the name of the subclass
        parametersNumber = self.getParameterNumber(className_)
        if parametersNumber > 0:  # check if the __init__ have more than or  0 parameter
            raise errors.TooManyParametersError("expected one parameter got " + str(parametersNumber))

        return className_

    def getAllMethodNames(self):
        """this method will get all the method names of the
        subclass given as className"""

        obj = self
        methods = inspect.getmembers(object=obj, predicate=inspect.ismethod)
        acceptedMethods = []

        for method in methods:

            if method[0].startswith(STARTING_NAME):  # check if the method name starts with The value in
                # STARTING_NAME or no

                parameterNumber = self.getParameterNumber(method[1])
                if parameterNumber != 0:  # because we make an object we should check it
                    # with parameterNumber 0
                    raise errors.TooManyParametersError(
                        "expected 0 parameter for " + method[0] + " got " + str(parameterNumber))

                acceptedMethods.append(method)

        return acceptedMethods



    def run(self):

        print("***start running tests in class ", self.className.__name__, '\n')
        for method in self.allMethods:
            self.runTest(testAddress=method[1], testName=method[0])
        print("***end running tests in class ", self.className.__name__, '\n')