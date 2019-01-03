# Reimplement the unique function implemented in the earlier examples using sets.

def unique2(x):
   x = list(set(x))
   print(x)

unique2([1,2,1,1,2,1,3])
unique2(['hello','Hello','ad','ad'])
