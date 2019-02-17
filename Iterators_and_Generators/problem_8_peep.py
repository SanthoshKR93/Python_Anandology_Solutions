# Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
listt = []
def peep(b):
   k = list(b)
   for i in k:
      listt.append(i)
   fe = k[0]
   print(fe,listt)

peep(iter(range(5)))
