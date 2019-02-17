import os
import sys
def tree(x,i=0):
   try:
      ls=os.listdir(x)
      k=0
      dirc = x.split("/")
      print (' '*i+'|'+dirc[-1])
      while k<len(ls):
         if '.' in ls[k]:
            print (' '*i + '|' + '-'*2 + ls[k])
         else:
            tree(x+'/'+ls[k],i+2)
         k=k+1
   except OSError:
      return 
tree(sys.argv[1])
