# Implement a function izip that works like itertools.izip.

def izip(a,b):
   return iter(zip(a,b))

v = izip(['a','b','c'],[1,2,3,4])
for i,j in v:
   print(i,j)
