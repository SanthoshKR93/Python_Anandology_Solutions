# Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?
# factorial(4) ------> 24

pdt = 1
def product(x):
   for i in x:
      global pdt
      pdt = pdt*i
   return pdt

def factorial(j):
   y = product(range(1,j+1))
   return y

m = factorial(4)
print(m)
