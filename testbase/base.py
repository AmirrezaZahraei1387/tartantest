"""base is the base class for all the testclasses that want to
run the tests. it gives some basic features to that"""
import time
import traceback
from termcolor import colored
import abc
from setUpers.setup import SetDown
import inspect


class Base(abc.ABC, SetDown):


    def __init__(self, allMethods):
        super().__init__(allMethods=allMethods)


    @staticmethod
    def getParameterNumber(obj: callable):
        """this function will simply give back the number of parameters of
        a callable object"""
        return len(inspect.signature(obj).parameters)

    @staticmethod
    def print_error_message(testName):
        print(colored("test failed at " + str(testName), "red"))
        print(colored(traceback.format_exc(), "red"))

    def runTest(self, testAddress, testName):
        startingTime = time.time()

        try:

            methods = self.runMethod(testName)  # getting the names off setup and takedown methods
            methods["setup"][1]()
            testAddress()
            methods["takedown"][1]()

        except Exception:
            self.print_error_message(testName)
        except BaseException:
            self.print_error_message(testName)
        else:
            print(colored("successfully ran test " + str(testName), "green"))

        endingTime = time.time()
        print(colored("ran test " + str(testName) + " in " + str(endingTime - startingTime) + "s", "green"))

        print("=======================================================================")

    @abc.abstractmethod
    def run(self):
        """this is the function that will run the test"""