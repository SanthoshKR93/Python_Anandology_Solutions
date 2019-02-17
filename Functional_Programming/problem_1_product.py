# Implement a function product to multiply 2 numbers recursively using + and - operators only.
pdt = 0
def product(a,b):
   if b == 0:
      return 0
   return a + product(a,b-1) 



pdt = product(23,5)

print(pdt)
