# Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.
# sum([1,2,3])   ----> 6
res=0
def sum(x):
   for i in x:
      global res
      res = res+i
   return res

y = sum([1,2,3])
print(y)

   

