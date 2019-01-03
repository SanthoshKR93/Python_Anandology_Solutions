# Write a program center_align.py to center align all lines in the given file.

import sys,math
a = sys.argv[1]
b = sys.argv[2]
s = ''
def center(fname):
   f = open(fname,'r')
   v = f.readlines()
   #print(v)
   m = max(v,key = len)
   n = len(m)
   #print(n)
   #print (m)	
   for i in v:
      i = i.strip("\n")
      #print (i)
      slen = (n - len(i)) / 2
      val = math.ceil(slen)
      #print (val)
      global s
      s = s + (' ' * val) + i + "\n"
      slen = 0
      val = 0
   print(s)
   f.close()

if (a == 'center' or a == 'CENTER'):
   center(b)
else:
   print("Wrong Input !! Try Again")          
