# Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions.
# What happens when you call your min and max functions with a list of strings?

def max(x):
   for i in range(len(x)-1):  
      if x[i] > x[i+1]:
         maxm = x[i]
         x[i+1] = x[i]
      else:
         maxm = x[i+1]
         
      i = i + 1
   print (maxm)

def min(x):
   for i in range(len(x)-1):  
      if x[i] < x[i+1]:
         minm = x[i]
         x[i+1] = x[i]
      else:
         minm = x[i+1]
         
      i = i + 1
   print (minm)

max([4,2,6,1,10])
min([4,1,6,2,10])

max(['python','xenial','a','b','x'])
min(['python','xenial','a','b','x'])

# when operated on strings, the min and max returns the minimum and maximum values according to the lexical order.

