# Write a function valuesort to sort values of a dictionary based on the key.

h = []
c = []
v = []
def valuesort(dict):
   for key,value in dict.items():
      c.append(value)
      h.append(key)
   print(c)
   print(h)
   for m in range(len(h)):
      va = []
      va = h[m]
      for j in range(len(h)):
         if va <= h[j]:
            h[m],h[j] = h[j],h[m]
            c[m],c[j] = c[j],c[m]
         else:
            continue
   for l in range(len(h)):
      v.append(c[l])
   print(v)
   

valuesort({'z': 1, 'y': 2, 'a': 3})
