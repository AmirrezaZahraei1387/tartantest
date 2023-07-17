"""sometimes you may need some codes to run
before a special test. in that case you can use the
setup. the setups will be two optional functions.
one work for setting up the environment needed for
the test and another one change the situation to the
normal one. for making the setups and takedowns you
should make a function starts with one of the following names
and end with test name. for example if we have a test named A,
the setup and takedown is like this

setupA
takedownA

note for every setup a takedown is needed respectively
"""

# here methods refer to both function and method
import setUpers.errors as errors


class SetDown:

    names: list = {"setup": "setup", "takedown": "takedown"}

    def __init__(self, allMethods):
        """these are the names of all  methods of class
        or functions containing both tests and other functions and methods"""

        self.__setDownMethods = []

        for method in allMethods:
            if method[0].startswith(self.names["setup"]) or method[0].startwith(self.names["takedown"]):
                self.__setDownMethods.append(method)

    def runMethod(self, nameMethod):

        setupMethod = self.names["setup"]+str(nameMethod)
        takedownMethod = self.names["takedown"]+str(nameMethod)

        try:
            self.__setDownMethods.index(setupMethod)
        except IndexError:
            setupMethod = False

        try:
            self.__setDownMethods.index(setupMethod)
        except IndexError:
            takedownMethod = False

        if setupMethod is False and takedownMethod is False:
            return 0

        elif setupMethod != takedownMethod:
            raise errors.BothSetupTakedownError("expected to provide both setup and takedown method/function")

        else:
            return {}








































