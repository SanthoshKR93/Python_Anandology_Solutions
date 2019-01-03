# Write a function unique to find all the unique elements of a list.

k = []
def unique(x):
   length = len(x)
   for i in range(length):
      global k
      if x[i] in k:
         continue
      else:
         k.append(x[i])
   
   print (k)
   k = []


# unique([1, 2, 1, 3, 2, 5])
#unique(["py","py","qw","ui","qwqwqwqwq","ui","UI"])
unique([['eat', 'eat', 'ate', 'ate', 'tea', 'tea'], ['done', 'node']]
)
# result is : [1, 2, 3, 5]

