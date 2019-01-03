# Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.
v = []
def even(x):
   if (x % 2 == 0):
      return 1 

def filter(func,val):	
   for i in val:
      j = func(i)
      if j == 1:
         v.append(i)
   print (v)

filter(even,range(10))

