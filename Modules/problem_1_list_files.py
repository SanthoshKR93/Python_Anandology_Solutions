# Write a program to list all files in the given directory.
import os
path = ''
f = []
def list_files():
   path = os.getcwd()
   return os.listdir(path)
   
f = list_files()
for i in f:
   print (i)   
