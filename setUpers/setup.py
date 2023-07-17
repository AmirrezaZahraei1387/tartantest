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


class SetDown:

    names:list = ["setup, takedown"]

    def __init__(self, allMethods):
        """these are the names of all  methods of class
        or functions containing both tests and other functions and methods"""

        for method in allMethods:
            if method[0].startswith(self.names[0]):


