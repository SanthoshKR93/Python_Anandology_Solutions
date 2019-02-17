# Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.

import os.path
import sys,os
n = 0
def dir_tree(ipath,j = 0):
   global n
   
   files = os.listdir(ipath)
   i = 0
   x = ipath.split("/")
   print (' '*j +'|'+'-' * 2+ x[-1])
   while i < len(files):
      if '.' in (files[i]):
         print(' '*n + '|'+'-' * 2 + files[i])
      else:   
         n = n+4
         #print(' '*i + '|' +'-' * 2 + files[i]+'/')
         dir_tree(ipath+'/'+files[i],j+2)
         
      i = i +1


dir_tree(sys.argv[1])
