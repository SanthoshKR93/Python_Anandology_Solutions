# Write a function dups to find all the duplicate elements of a list.

k = []
j = []
def dups(x):
   length = len(x)
   for i in range(length):
      global k,j
      if x[i] in k:
         j.append(x[i])
      else:
         k.append(x[i])
   
   print (j)
   k = []
   j = []


dups([1, 2, 1, 3, 2, 5])

# result is : [1, 2]

