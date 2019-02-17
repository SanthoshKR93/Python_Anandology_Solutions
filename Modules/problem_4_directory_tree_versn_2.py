# Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os,sys
from os.path import join,isfile
d = []
listt = []
val = ''
g = ''
def dir_tree(dlist,v = 0):
   
   d = dlist.split("/")
   val = d[-1]
   #print(d)
   listt = os.listdir(dlist)
   n = 0
   print ('  '*v,val)
   while n < len(listt):
      if '.' in listt[n]:
         print(" " * v,"|","-" * 2,listt[n])
      else:
         #g = os.path.join(dlist,listt[n])
         dir_tree(dlist + '/' + listt[n],v + 2)
      n = n + 1


dir_tree(sys.argv[1])



