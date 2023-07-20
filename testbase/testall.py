"""sometimes you have a lot of tests, and you want to run all of
them together instead running each test file individually, for
example you have 10 python files containing unittest, and
you want to run all of them. in that case it can help
you do the same thing that you want.

to do this you have two options
1 - giving the path of each test file manually
2 - giving the path of directory containing all the tests"""
import subprocess
import pathlib
import os


def fileRun(pathFiles: list):

    for path in pathFiles:
        betterPath = pathlib.Path(path).absolute()
        subprocess.run(["python", str(betterPath)])


def dirRun(pathDir):

    pathFiles = os.listdir(pathDir)

    for index in range(len(pathFiles)):
        pathFiles[index] = pathlib.Path(pathDir+"/"+pathFiles[index]).absolute()

    fileRun(pathFiles)

