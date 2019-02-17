# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

import sys,os
def printlines(f_list):
   for i in f_list:
      f = open(i)
      cont = f.readlines()
      for j in cont:
         if len(j) > 40:
            print(j)
         else:
            continue

printlines(sys.argv[1:])
