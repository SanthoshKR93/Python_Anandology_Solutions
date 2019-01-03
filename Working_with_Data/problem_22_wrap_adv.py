# The above wrap program is not so nice because it is breaking the line at middle of any word.
# Can you write a new program wordwrap.py that works like wrap.py,but breaks the line only at the word boundaries?

import sys
a = sys.argv[1]
b = sys.argv[2]
c = int(sys.argv[3])
s = ""
length = 0
def wrap(fname,width):
   f = open(fname,'r')
   v = f.read().split(" ")
   #print (v)
   #print (len(f.read().split(' ')))
   global length,s
   for i in v:
      #print (len(i))
      i.strip("\n")
      length = length + len(i) + 1
      if length <= width:
         s = s + i + ' '
      elif length > width:
         s = s + '\n' + i + ' '   
         length = len(i)+1
      else:
         print ("error : out of index bounds")
   print (s)
   

if (a == 'wrap' or a == 'WRAP'):
   wrap(b,c)

else:
   print("Wrong input !!! try again")
