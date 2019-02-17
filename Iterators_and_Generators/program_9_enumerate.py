#The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.


s = []
k = []
j = []
def enumerate(listt):
   v = len(listt)
   x = [(x,y) for x in range(v) for y in listt]
   print(x)
   print(len(x))
   c = len(x)
   k = [j for j in range(0,c,v+1)]
   print (k)
   for i in k:
      s.append(x[i]) 
   print(tuple(s))
enumerate(['a','b','c','d','e'])
