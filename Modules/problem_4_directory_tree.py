# Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os
from os.path import join,isfile
path =''
f = []
f1 = []
y = []
z = []
path0 = os.getcwd()
pathreset = os.getcwd()
path1 = ''
value =[]
count = 0
def printer(y):
   global count
   for m in y:
      if os.path.isfile(m):
         zv =''
         if m == y[-1]:
            zv = "|  " * count +" " * count + "\\" + "--" + m
         else:
            zv = "|" +"  " * count + "|" * count  + "--" + m
         z.append(zv)
         #print(z)
      elif not os.path.isfile(m):
         global path0
         if m in y :
            zv = ''
            
            zv ="|" +"  " * count + "|" * count + "--" + m
            count = count + 1
            z.append(zv)
            #print(z)
            path1 = os.path.join(path0,m)
            #print(path0)
            #print(path1)
            path0 = path1
            #print(m)
            fi = os.listdir(path1)
            os.chdir(path1)
            #print(fi)
            printer(fi)
         else:
            break
      else:
         break
      path0 = pathreset
      #print(path0)
      os.chdir(path0)
      count = 0
   #print(z)
   return z
def dir_tree():
   path = os.getcwd()
   f = os.listdir(path)
   #print(f)
   value = printer(f)
   for dj in value:
      print(dj)      
dir_tree()         
