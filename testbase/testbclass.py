"""the testb is a file that is implemented to make
the most important part of the library.
this file will have a class named TestB that can be inherited from
the class containing the tests. it will run the tests.
the class will run the tests by getting the names of
methods inside that starts with test word. this because of
this reason to find the methods that are not tests and probably
have parameters."""
import inspect
import time
import traceback
from termcolor import colored
import errors

# this is the constants that defines the name that must come first in the method name of subclass that
# contain tests
STARTING_NAME = "testb"


class TestBClass:

    @staticmethod
    def checkClass():
        """this method will check if the subclass meet the requirements
        or no.
        1 - one checking if one exist or no
        2 - checking if its constructor has exactly 1 parameter"""

        className = TestBClass.__subclasses__()  # here we are getting the name of the subclass
        if len(className) == 1:  # making sure there is exactly one subclass
            className = className[0]
        else:
            raise errors.NotOneSubClassError("expected exactly one subclass got " + str(className))

        parametersNumber = len(inspect.signature(className).parameters)
        if parametersNumber > 0:  # check if the __init__ have more than or  0 parameter
            raise errors.TooManyParametersError("expected one parameter got " + str(parametersNumber))

        return className

    @staticmethod
    def getAllMethodNames(className):
        """this method will get all the method names of the
        subclass given as className"""

        obj = className()
        methods = inspect.getmembers(object=obj, predicate=inspect.ismethod)
        acceptedMethods = []

        for method in methods:

            if method[0].startswith(STARTING_NAME):  # check if the method name starts with The value in
                # STARTING_NAME or no

                parameterNumber = len(inspect.signature(method[1]).parameters)
                if parameterNumber != 0:  # because we make an object we should check it
                    # with parameterNumber 0
                    raise errors.TooManyParametersError(
                        "expected 0 parameter for " + method[0] + " got " + str(parameterNumber))

                acceptedMethods.append(method)

        return acceptedMethods

    def run(self):

        className = self.checkClass()  # if the subclass is not something we want error is raised
        allMethods = self.getAllMethodNames(className=className)  # the output is similar to this:
        # [(methodName, methodAddress), (methodName, methodAddress), ... ]

        for method in allMethods:

            startingTime = time.time()

            try:
                method[1]()
            except Exception:
                print(colored("test failed at " + str(method[0]), "red"))
                print(colored(traceback.format_exc(), "red"))
            else:
                print(colored("successfully ran test " + str(method[0]), "green"))

            endingTime = time.time()
            print(colored("ran test " + method[0] + " in " + str(endingTime - startingTime) + "s", "green"))

            print("=======================================================================")
