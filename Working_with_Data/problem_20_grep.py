# Implement unix command grep. The grep command takes a string and a file as arguments and 
# prints all lines in the file which contain the specified string.


import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

def grep(fname,key):
   f = open(fname,'r')
   v = f.readlines()
   global b
   c = []
   for i in range(len(v)):
      if b in v[i]:
         c.append(v[i])
   
   print("".join(c))

if (a == 'grep' or a == 'GREP'):
   grep(c,b)
else:
   print("wrong input!!! try again")

