"""in this code file we implement different forms of
assertions for the tests that are written. they are implemented
as functions and not classes, and they can raise an error
when they are not satisfied with the given input."""
import errors


def ifEqual(first, second, description=""):
    """check if the first and second are equal.
    otherwise raise error and show the descriptions.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""

    if second != first:
        raise errors.FailAssertionError("second == first", first, second, "{}=={}", "ifEqual", description)


def ifnEqual(first, second, description=""):
    """check if the first and second are equal.
    otherwise raise error and show the descriptions.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""

    if second == first:
        raise errors.FailAssertionError("second != first", first, second, "{}!={}", "ifnEqual", description)


def failTest(description=""):
    """fail the test that is wanted, however it won't terminate
    all the tests in the class"""
    raise errors.preFailError("failtest", description)


def failAllTests(description=""):
    """failing all the tests in  the class. in  that case the other tests
    will never run  on that class"""
    raise errors.preFailError("failall", description)


def ifTrue(first, description=""):
    """check if the given object named first is true or not. if true it
    means success otherwise fail.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if not first:
        raise errors.FailAssertionError("first == True", bool(first), "", "{}==True{}", "ifTrue", description)


def ifFalse(first, description=""):
    """check if the given object named first is false or not. if false it
    means success otherwise fail.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if first:
        raise errors.FailAssertionError("first == False", bool(first), "", "{}==False{}", "ifFalse", description)


def ifNone(first, description=""):
    """check if the given object named first is None or not. if None it
    means success otherwise fail.
    do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if first is None:
        raise errors.FailAssertionError("first == None", first, "", "{}==None{}", "ifNone", description)


def ifInstance(first, second, description=""):
    """check if the given object named first is an instance of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if not isinstance(first, second):
        raise errors.FailAssertionError("isinstance(first, second)", first, second, "isinstance({},{})", "ifInstance",
                                        description)


def ifnInstance(first, second, description=""):
    """check if the given object named first is not an instance of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if isinstance(first, second):
        raise errors.FailAssertionError("not isinstance(first, second)", first, second, "not isinstance({},{})",
                                        "ifnInstance",
                                        description)


def ifSubClass(first, second, description=""):
    """check if the given class named first is a subclass of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if not issubclass(first, second):
        raise errors.FailAssertionError("issubclass(first, second)", first, second, "issubclass({},{})",
                                        "ifSubClass",
                                        description)


def ifnSubClass(first, second, description, do, elseDo):
    """check if the given class named first is not a subclass of the class
    second or not.
        do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if issubclass(first, second):
        raise errors.FailAssertionError("not issubclass(first, second)", first, second, "not issubclass({},{})",
                                        "ifnSubClass",
                                        description)


def ifIn(first, second, description=""):
    """check if the first is in second using python in operator.
            do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if first not in second:
        raise errors.FailAssertionError("first in second", first, second, "{} in {}",
                                        "ifIn",
                                        description)


def ifnIn(first, second, description=""):
    """check if the first is not in second using python not in operator.
            do is function that will be executed if test go true and
    elseDo is a function that will be executed otherwise"""
    if first in second:
        raise errors.FailAssertionError("first not in second", first, second, "{} not in {}",
                                        "ifnIn",
                                        description)






