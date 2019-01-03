# Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

import sys
j = 0
a = sys.argv[1]
b = sys.argv[2]
c = int(sys.argv[3])
s = ""
def wrap(fname,width):
   cw = width
   f = open(fname,'r')
   v = f.read()
   global j,s
   while (width <= len(v)):
      for i in range(width)[j:]:
         s = s + v[i]
      j = width
      width = width + cw
      print (s)
      s = ""
      
   f.close()
if (a == 'wrap' or a == 'WRAP'):
   wrap(b,c)
else:
   print("Wrong input !!! Try again")
