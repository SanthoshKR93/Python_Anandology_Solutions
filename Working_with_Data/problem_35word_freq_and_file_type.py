# Can you use word frequency to tell whether the given file is a Python program file, C program file or a text file?

import sys
filename = sys.argv[1]
v = {}
words = ''
c = []
h = []
py=['print','def','items()','import']
cpgm=['printf("','#include','<stdio.h>','#include<stdlib.h>','scanf("','getchar();','EOF',]
cpy = 0
ccpgm = 0
def read_words(filename):
   f = open(filename)
   words = f.read().split()
   return words

def word_freq(words):
   dict ={}
   for i in words:
      dict[i] = dict.get(i,0) + 1
   return dict

def file_type(dict):
   for key,value in dict.items():
      c.append(value)
      h.append(key)
   for m in range(len(c)):
      for j in range(len(c)):
         if c[m] >= c[j]:
            c[m],c[j] = c[j],c[m]
            h[m],h[j] = h[j],h[m]
         else:
            continue
   for l in h:
      global cpy,ccpgm
      if l in py:
         cpy=cpy+1
      elif l in cpgm:
         ccpgm=ccpgm+1
      else:
         continue
   if cpy>ccpgm:
      print ("python file")
   elif ccpgm>cpy:
      print("c file")
   else:
      print("text file")
v = word_freq(read_words(filename))
file_type(v)

