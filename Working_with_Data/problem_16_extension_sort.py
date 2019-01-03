# Write a function extsort to sort a list of files based on extension.
y = []
def extsort(x):
   for i in range(len(x)):
      y.append(x[i].split('.'))
   y.sort(key=lambda n: n[1])
   v = len(x)
   x = []
   for j in range(v):
      x.append(".".join(y[j]))
   print(x)

extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
