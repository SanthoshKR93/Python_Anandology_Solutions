# Write a function reverse to reverse a list. Can you do this without using list slicing?
# reverse([1, 2, 3, 4]) -----> [4, 3, 2, 1]

def reverse(x):
   length = len(x)-1
   k = list(range(len(x)))
   for i in x:

      k[length]=i
      length=length-1
   return k

y = reverse([1,2,3,4])
print (y)
