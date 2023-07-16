"""in this code file we implement different forms of
assertions for the tests that are written. they are implemented
as functions and not classes, and they can raise an error
when they are not satisfied with the given input."""


def ifEqual(first, second, descriptions, do, elseDo):
    """check if the first and second are equal.
    otherwise raise error and show the descriptions.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""

    if second != first:
        pass
        # raising error


def ifnEqual(first, second, descriptions, do, elseDo):
    """check if the first and second are equal.
    otherwise raise error and show the descriptions.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""

    if second == first:
        pass
        # raising error


def failTest(descriptions, do):
    """fail the test that is wanted, however it won't terminate
    all the tests in the class"""
    # raising error


def failAllTests(descriptions, do):
    """failing all the tests in  the class. in  that case the other tests
    will never run  on that class"""
    # raising error


def ifTrue(first, description, do, elseDo):
    """check if the given object named first is true or not. if true it
    means success otherwise fail.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifFalse(first, description, do, elseDo):
    """check if the given object named first is false or not. if false it
    means success otherwise fail.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifNone(first, description, do, elseDo):
    """check if the given object named first is None or not. if None it
    means success otherwise fail.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifInstance(first, second, description, do, elseDo):
    """check if the given object named first is an instance of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifnInstance(first, second, description, do, elseDo):
    """check if the given object named first is not an instance of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifSubClass(first, second, description, do, elseDo):
    """check if the given class named first is a subclass of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifnSubClass(first, second, description, do, elseDo):
    """check if the given class named first is not a subclass of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifIn(first, second, descriptions, do, elseDo):
    """check if the first is in second using python in operator.
            do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""


def ifnIn(first, second, descriptions, do, elseDo):
    """check if the first is not in second using python not in operator.
            do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""

