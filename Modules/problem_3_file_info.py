# Write a program to list all the files in the given directory along with their length and last modification time.
# The output should contain one line for each file containing filename, length and modification date separated by tabs.
import os
from os.path import isfile
import time
path = ''
f = []
def file_info():
   path = os.getcwd()
   f = os.listdir(path)
   for i in f:
      if isfile(i):
         s = os.stat(i)
         print (i + '\t' * 2 + str(s.st_size) + '\t' + time.ctime(s.st_mtime) )


file_info()
