#!/usr/bin/python
#filename:learn_python.y

from sys import *
import os
import time


print __name__ #show whether the module is called

class myfirstclass:
    """build a class a object
    """
print(myfirstclass.__doc__) #print the docstring of class
o = myfirstclass()

import os
print "OS name = ",os.name

for key in os.environ:
    print "key = %s \t\t\t\t value = %s "% (key,os.environ[key])

#os.rename("./test","./test") 
    #change the dir name
#os.rename("./test1/index.rst","./test1/index-1.rst")
    # change the file name
