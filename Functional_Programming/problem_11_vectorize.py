# Write a function vectorize which takes a function f and return a new function, which takes a list as argument and 
# calls f for every element and returns the result as a list.

def vectorize(func):
   res = []
   def g(x):
      for i in x:
         res.append(func(i))
      return res
   return g

v = vectorize(len)

print(v([[1, 2], [2, 3, 4]]))
   
