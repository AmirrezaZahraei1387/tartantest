# TartanTest

tartantest is a python project that will make the process of writing unittests 
in python faster and easier for you. as you that in unittest you should test each part individually.
now in this library you can get a lot of tools that make this process faster.
the option of this library for working toward the unittest are the following 
basically.

#### 1 - showing the time it took to run the scripts
#### 2 - adding different types of asserting to each test
#### 3 - giving you the ability to run lots of tests in different files all together
#### 4 - run each tests you write individually and show each of them errors without stopping when a test went wrong
#### 5 - generating a meaningful messages about what happened
#### 6 - run your tests in both classes and functions


## Assertions
there are a lot of assertion types that this framework supports here are all of them 
all together by their parameters.

```python
from pyasserts.asserts import*

ifEqual(first, second, description="")
ifnEqual(first, second, description="")
failTest(description="")
failAllTests(description="")
ifTrue(first, description="")
ifFalse(first, description="")
ifNone(first, description="")
ifInstance(first, second, description="")
ifnInstance(first, second, description="")
ifSubClass(first, second, description="")
ifnSubClass(first, second, description, do, elseDo)
ifIn(first, second, description="")
ifnIn(first, second, description="")
```

however if the assertion you want is not in the list you can use the failTest to do so.

## Writing Tests as Classes

in this framework you can run your tests as both classes and functions.
to write you test as classes you should first import the following to you program

```python
from testbase import TestBClass
```

then inherit the class that will contain you tests

```python
from testbase import TestBClass

class MyTest(TestBClass):
    pass
```

now you can write down you tests in the class using assertions and any other exceptions.

```python
from testbase import TestBClass
from pyasserts import asserts

class MyTest(TestBClass):
    
    def testb_Addition(self):
        a = 6+3
        asserts.ifEqual(a, 9, "the addition is not working")
        
    def testb_TypeInt(self):
        a = int(45)
        asserts.ifInstance(a, int, "the int type have problem")

```

#### note: your test methods must all start with the identifier name "testb"

now for running you test simply use the run method like the following

```python
from testbase import TestBClass
from pyasserts import asserts

class MyTest(TestBClass):
    
    def testb_Addition(self):
        a = 6+3
        asserts.ifEqual(a, 9, "the addition is not working")
        
    def testb_TypeInt(self):
        a = int(45)
        asserts.ifInstance(a, int, "the int type have problem")

if __name__ == "__main__":
    test = MyTest()
    test.run()
```

it should run and print some text in console like the following

``` text
***start running tests in class  MyTest 

successfully ran test testb_Addition
ran test testb_Addition in 0.0s
=======================================================================
successfully ran test testb_TypeInt
ran test testb_TypeInt in 0.0s
=======================================================================
***end running tests in class  MyTest 
```

## Writing Tests as Functions

in order to run tests as functions first import the TestBFunc to program.

```python
from testbase import TestBFunc
```

now make an object from class TestBFunc and use the decorator addFunc to add the test
functions to the class main list.
#### Note: class TestBFunc have parameter named main that will be the name of the set of tests you have when showing messages in console

```python
from testbase import TestBFunc
from pyasserts import asserts

obj = TestBFunc("my first tests")

@obj.addFunc
def testb_Addition():
    a = 6+3
    asserts.ifEqual(a, 9, "the addition is not working")
  
@obj.addFunc
def testb_TypeInt():
    a = int(45)
    asserts.ifInstance(a, int, "the int type have problem")
```

finally use the run method to run the tests

```python
from testbase import TestBFunc
from pyasserts import asserts

obj = TestBFunc("my first tests")

@obj.addFunc
def testb_Addition():
    a = 6+3
    asserts.ifEqual(a, 9, "the addition is not working")
  
@obj.addFunc
def testb_TypeInt():
    a = int(45)
    asserts.ifInstance(a, int, "the int type have problem")

if __name__ == "__main__":
    obj.run()
```

it should run and make a message like the following in your console
```text
***start running function tests named  my first tests 

successfully ran test testb_Addition
ran test testb_Addition in 0.0s
=======================================================================
successfully ran test testb_TypeInt
ran test testb_TypeInt in 0.0s
=======================================================================
***end running function tests named  my first tests 
```

## setups and takedowns

sometimes you need to run some codes after and before you tests to make the needed conditions 
for your tests. in order to write a setup and a takedown for your tests you can put the name
setup or takedown in the first of the name of your test. for example a setup and a takedown 
for method/ function mytest will be setupmytest and takedownmytest.

```python
from testbase import TestBFunc
from pyasserts import asserts

obj = TestBFunc("my first tests")

# ++++++++++++++++++++++++++
@obj.addFunc
def setuptestb_Addition():
    print("start testb_Addition")

@obj.addFunc
def testb_Addition():
    a = 6+3
    asserts.ifEqual(a, 9, "the addition is not working")
    
@obj.addFunc
def takedowntestb_Addition():
    print("end testb_Addition")
# +++++++++++++++++++++++++++
    
    
@obj.addFunc
def setuptestb_TypeInt():
    print("start testb_TypeInt")
    
@obj.addFunc
def testb_TypeInt():
    a = int(45)
    asserts.ifInstance(a, int, "the int type have problem")
    
@obj.addFunc
def takedowntestb_TypeInt():
    print("end testb_TypeInt")
# ++++++++++++++++++++++++++

if __name__ == "__main__":
    obj.run()
```

and for classes:

```python
# functest.py
from testbase import TestBClass
from pyasserts import asserts

class MyTest(TestBClass):

# ++++++++++++++++++++++++++
    def setuptestb_Addition(self):
        print("start testb_Addition")

    def testb_Addition(self):
        a = 6+3
        asserts.ifEqual(a, 9, "the addition is not working")
    
    def takedowntestb_Addition(self):
        print("end testb_Addition")
# +++++++++++++++++++++++++++
    
    
    def setuptestb_TypeInt(self):
        print("start testb_TypeInt")
    
    def testb_TypeInt(self):
        a = int(45)
        asserts.ifInstance(a, int, "the int type have problem")

    def takedowntestb_TypeInt(self):
        print("end testb_TypeInt")
# ++++++++++++++++++++++++++

if __name__ == "__main__":
    test = MyTest()
    test.run()
```

## Running MultipleTests in Different Files
```python
# functest.py
from testbase import TestBFunc
from pyasserts import asserts

obj = TestBFunc("my first tests")

# ++++++++++++++++++++++++++
@obj.addFunc
def setuptestb_Addition():
    print("start testb_Addition")

@obj.addFunc
def testb_Addition():
    a = 6+3
    asserts.ifEqual(a, 9, "the addition is not working")
    
@obj.addFunc
def takedowntestb_Addition():
    print("end testb_Addition")
# +++++++++++++++++++++++++++
    
    
@obj.addFunc
def setuptestb_TypeInt():
    print("start testb_TypeInt")
    
@obj.addFunc
def testb_TypeInt():
    a = int(45)
    asserts.ifInstance(a, int, "the int type have problem")
    
@obj.addFunc
def takedowntestb_TypeInt():
    print("end testb_TypeInt")
# ++++++++++++++++++++++++++

if __name__ == "__main__":
    obj.run()
```

```python
#classtest.py
from testbase import TestBClass
from pyasserts import asserts

class MyTest(TestBClass):

# ++++++++++++++++++++++++++
    def setuptestb_Addition(self):
        print("start testb_Addition")

    def testb_Addition(self):
        a = 6+3
        asserts.ifEqual(a, 9, "the addition is not working")
    
    def takedowntestb_Addition(self):
        print("end testb_Addition")
# +++++++++++++++++++++++++++
    
    
    def setuptestb_TypeInt(self):
        print("start testb_TypeInt")
    
    def testb_TypeInt(self):
        a = int(45)
        asserts.ifInstance(a, int, "the int type have problem")

    def takedowntestb_TypeInt(self):
        print("end testb_TypeInt")
# ++++++++++++++++++++++++++

if __name__ == "__main__":
    test = MyTest()
    test.run()
```

suppose that we have the two above files for testing our program. running all of them
is not a very big task, however as the projects get bigger, the tests will also get bigger.
In that case running all of them is very hard. Now here you use fileRun and DirRun to run you
tests.

the fileRun will get the names of all test files as one single list and run them however the
dirRun will get the directory that contains all tests, and then it will run them.

for example:
```python
#classtest.py
from testbase.testall import fileRun
fileRun(["classtest.py", "functest.py"])
```
or when you put your tests inside a directory you can use this:
```python
#classtest.py
from testbase.testall import dirRun
dirRun("tests") # directory name. we supposed it is named tests
```





