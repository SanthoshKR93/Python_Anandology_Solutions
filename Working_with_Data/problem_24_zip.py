# Provide an implementation for zip function using list comprehensions.


f = []
s = []
final = []
def zip(f,s):
   n = len(s)
   m = len(f)
   for i in range(n):
      fin = []
      fin.append(f[i])
      fin.append(s[i])
      #print (fin)
      final.append(tuple(fin))
   print (final)

zip([1, 2, 3], ["a", "b", "c"])
