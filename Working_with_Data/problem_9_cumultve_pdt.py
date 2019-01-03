# Write a function cumulative_product to compute cumulative product of a list of numbers.

pdt = 1
k = []
def cumulative_product(x):
   a=type(x[0])
   b=type(1)
   c=type('hello')
   for i in range(len(x)):
      if a==b:
         global pdt
         pdt = pdt * x[i]
         global k
         k.append(pdt)
      else:
         print("wrong type")
   print(k)
   k = []
   pdt = 1

cumulative_product([1,2,3,4])
cumulative_product([4,3,2,1])
