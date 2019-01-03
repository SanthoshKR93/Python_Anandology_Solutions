# Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.
s = []
k = []
j = []
def enumerate(listt):
   v = len(listt)
   x = [(x,y) for x in range(v) for y in listt]
   #print(x)
   #print(len(x))
   c = len(x)
   k = [j for j in range(0,c,v+1)]
   #print (k)
   for i in k:
      s.append(x[i]) 
   print(s)
enumerate(['a','b','c','d','e'])
