'''
Joshua Wren
28 January 2021
Simple Class Example
'''

from __future__ import print_function
import sys


class systemInfo:
    '''
    Simple SystemInfo Class that obtains
    the major python version and the
    operating system type
    '''

    def __init__(self):
        # Create object variables and Constants
        if sys.version_info[0] < 3:
            self.PYTHON_VERSION = 2
        else:
            self.PYTHON_VERSION = 3

        self.OS = sys.platform

    def PrintSysInfo(self):
        # Print out the system information
        print(self.PYTHON_VERSION)
        print(self.OS)


# create an object
sysInfo = systemInfo()

# print the attribute PYTHON_VERSION
print(sysInfo.PYTHON_VERSION)
# print the attribute OS
print(sysInfo.OS)

# invoke the object PrintSysInfo Method
sysInfo.PrintSysInfo()
