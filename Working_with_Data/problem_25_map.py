# Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.

v = []
def square(x):
   return(x*x)

def map(func,val):
   for i in val:
      v.append(func(i))
   print (v)

map(square,range(5))
   
