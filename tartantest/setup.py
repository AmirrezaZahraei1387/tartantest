from setuptools import setup, find_packages

setup(
    name='tartantest',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'termcolor'
    ],
    extras_require={
        'opt1': ['serial'],
        'opt2': ['pyserial'],
    }
)