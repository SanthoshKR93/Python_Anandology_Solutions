# Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os
def findfiles(x):
   path = os.getcwd()
   v = os.walk(path)
   #print(list(v))
   for gpath,gdir,gfile in v:     # path directory file format
      if x in gfile:
         print (os.path.join(gpath,x))

findfiles("2.txt")
