# Implement unix commands head and tail. The head and tail commands take a file as argument and 
# prints its first and last 10 lines of the file respectively.

import sys
a = sys.argv[1]
b = sys.argv[2]

def head(fname):
   f1 = open(fname)
   hlist = f1.readlines()
   nlist=[]
   nlist = hlist[0:10]
   #print(nlist)
   
   print ("".join(nlist))
   f1.close()
def tail(fname):
   f2 = open(fname,'r')
   tlist = f2.readlines()
   mlist=[]
   mlist = tlist[-10:]
   #print(mlist)
   
   print ("".join(mlist))
   f2.close()

if (a == 'head'):
   head(b)
elif (a == 'tail'):
   tail(b)
else:
   print("wrong input!! please try again...")
