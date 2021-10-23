"""
Modules - import code of other fileo for make a function
in our code

1- Logically organize your Python code
2- Module should contain related code

"""

#is just .py file
#create module for make to sum between two numbers

import modules

modules.ask()

print("\n")
#we can import of a module a specific function of this

from modules import divide

Divide = divide()
print(Divide)
print("\n")

#we can import of a module a specific variable
from modules import Hallo

print(Hallo)

#we can import function and varibles to same time

from modules import divide, Hallo

#or import all the module

from modules import *

#we can abretiature the name of the module

import modules as m

m.ask()

#Built-In python modules: exist different modules of python
#Example:

#module math, operation mathematical
import math 

power = math.pow(2, 4)

#module date time

from datetime import datetime, timezone

day_now = datetime.now()
