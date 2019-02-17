# Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print
# documentation for the module and each of the functions defined in that module.

from inspect import isfunction
import sys
def my_doc(mod):
   m = __import__(mod)
   #print("DESCRIPTION: \n" ,m.__doc__,"\n FUNCTIONS: \n")
   for i in dir(m):
      print (i)
        

my_doc(sys.argv[1])
