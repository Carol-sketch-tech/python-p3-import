# import 

'''
importing modules using absolute and relative imports.
Module - is a file containing python definations and statements. 
a modiles functions, classes and global variables can be accessed by other methods.

package is a collection of modules that can be accessed as a group using the package name.
import -> the python keyword used to access data from other packages and modules inside of the current module.
'''

# as the program gets longer one might want to split them into several files for easire mainrtainance.
# you may also wasnt to use a handy fucntion that youve written in several programs without copying its defination
# into each programs, or functions that others wrote to save you abit of development time.
# 
# all imports start from files(also called modules)
# using import keyword,we can access whole modules or the classes functions and objects inside from any other module.#


# IMPORTING A MODULE.
'''
a module may have multiple fucntions and definations. what if we only want to use a few of them
a more conciense way of importing is only importing the things we need.
say we want to import the name property in the os module. we can do this using the from keyword.
'''
# from os import name
from os import *

print(name)
'''
notice we did not need to repeat the os word, the from keyword also allows us to import everything
form the library using the * operator.
however this is not the best may or method to use because for example, we called another varibale name?
this woudl lead to less concise and you ame runinto namespace issues.
when we use the * operator we do not know exactly what we are taking from the module, leading to less 
readable code.
'''

# ABSOLUTE IMPORTS.
'''
an absolute import specifies the module to be imported using hte full path from the project root directory.
'''

# example of an absolute import -> when imported we specify the path of the import from the root directory.
# say we have an class called function1 

class funciton1:
    def __init__(self,name):
        self.name= name 

        # when we want to import this file into another file, we import it as follows 
# when its path from the root directory is as follows package1, module1 
from package1.module1 import function1

# module6 six is buried deep to import its function1().we will need to crawl through subpackage1/ in package2

from package2.subpackage1.module6 import function1

# the following is how you call a function in python
print (fucntion1())# this is an example of calling a function that has no paramater or argument passed.

# PROS AND CONS OF ABSOLUTE IMPORTS.
'''
absolute imports remain valid even if the current location statement chages and they make it easy to 
see exaclty where the resource is coming from.

when should one not use imports
-> lets say we want to use imports a module from a long nested directory structure.
the import statement would be huge.
using long import statemetns can be avoided by using relative imports.
'''

# RELATIVE IMPORTS.
'''
the reason relative imports exist is because they allows us to arrange the structure of larfe packages without hacving to edit
sub-packages.
if we rearrange all the packages with abosolute imports, we have to change all the paths in every files import statement so match the new location.

'''
# module 1
def function1():
    print('this is fucntion 1')

from .module1 import function1

# we can also run module2 as a module using hte following commands.
# python3 -m subpackage1.subpackage2.module2
'''
relative imports only work when we use them in a module. whis is when we need to include the -m arguments
relative imports cannot be invoked in scripts.

if you need to go up multiple levels in the directory struture you can use additional dots.

in modu;e 2 we can import module3 using two dots which represents the parent directory that module3 is in.
relative imports are greate if you hvae lots of code files that are related but it can be unclear to other deelopers which modules are kept where.
'''