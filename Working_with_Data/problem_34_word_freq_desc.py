# Improve the above program to print the words in the descending order of the number of occurrences.

import sys
filename = sys.argv[1]
v = {}
words = ''
c = []
h = []
def read_words(filename):
   f = open(filename)
   words = f.read().split()
   return words

def word_freq(words):
   dict ={}
   for i in words:
      dict[i] = dict.get(i,0) + 1
   return dict

def sort_dict(dict):
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
   for l in range(len(h)):
      print(h[l],c[l])

v = word_freq(read_words(filename))

sort_dict(v)
#for key,value in v.items():
 #  print(key,value)
