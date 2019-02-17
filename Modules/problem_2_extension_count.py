# Write a program extcount.py to count number of files for each extension in the given directory. 
# The program should take a directory name as argument and print count and extension for each available file extension.

import os
from os.path import isfile
f = []
path = ''
fdict = {}
b = []
def extension_count():
   path = os.getcwd()
   f = os.listdir(path)
   for i in f:
      if isfile(i):
         a = []
         a = i.split(".")
         b.append(a)
   for j in b:
      fdict[j[-1]] = fdict.get(j[-1],0) + 1
   for key,value in fdict.items():
      print(key,value)

extension_count()
