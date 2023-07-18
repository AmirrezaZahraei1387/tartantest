"""base is the base class for all the testclasses that want to
run the tests. it gives some basic features to that"""
import time
import traceback
from termcolor import colored
from setUpers.setup import SetDown
import inspect
from setUpers import errors



class Base(SetDown):

    testFailed = -1
    testOk = 1

    def __init__(self, allMethods):
        super().__init__(allMethods=allMethods)

    def methodRunner(self, method, testName):

        try:
            method()
        except Exception:
            self.print_error_message(testName)

        except BaseException:
            self.print_error_message(testName)

        else:
            print(colored("successfully ran test " + str(testName), "green"))


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

        try:
            methods = self.runMethod(testName)  # getting the names off setup and takedown methods

        except errors.BothSetupTakedownError:
            self.print_error_message(testName)
            return self.testFailed

        startingTime = time.time()
        if methods != self.noSetDown:
            self.methodRunner(methods["setup"][1], methods["setup"][1].__name__)
            self.methodRunner(testAddress, testName)
            self.methodRunner(methods["takedown"][1], methods["takedown"][1].__name__)
        else:
            self.methodRunner(testAddress, testName)
        endingTime = time.time()

        print(colored("ran test " + str(testName) + " in " + str(endingTime - startingTime) + "s", "green"))
        print("=======================================================================")












