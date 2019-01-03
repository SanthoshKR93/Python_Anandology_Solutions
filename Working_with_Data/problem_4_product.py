# Implement a function product, to compute product of a list of numbers.
# product([1, 2, 3]) -----> 6

pdt = 1
def product(x):
   for i in x:
      global pdt
      pdt = pdt*i
   return pdt

y = product([1, 2, 3])
print(y)
